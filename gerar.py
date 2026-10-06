#!/usr/bin/env python3
"""Gera index.html — portfólio de Alexandre Cajazeira.

    python gerar.py

Fontes: fonte/perfil.yaml (dados públicos do autor e seções), fonte/trabalhos.yaml (trabalhos
anteriores) e fonte/template.html (layout). Depende só de PyYAML (pip install pyyaml).
O resultado é uma página estática servida pelo GitHub Pages a partir da raiz do repositório.
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent


def ler_yaml(caminho: Path):
    return yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}


def main() -> Path:
    perfil = ler_yaml(RAIZ / "fonte" / "perfil.yaml")
    trabalhos = ler_yaml(RAIZ / "fonte" / "trabalhos.yaml") or []
    dados = {"perfil": perfil, "trabalhos": trabalhos, "gerado_em": dt.date.today().isoformat()}
    descricao = " · ".join(x for x in (perfil.get("cargo"), perfil.get("instituicao")) if x)
    html = ((RAIZ / "fonte" / "template.html").read_text(encoding="utf-8")
            .replace("__DADOS__", json.dumps(dados, ensure_ascii=False, default=str))
            .replace("__NOME__", perfil.get("nome", "Portfólio"))
            .replace("__DESCRICAO__", descricao.replace('"', "&quot;"))
            .replace("__URL__", perfil.get("url") or ""))
    saida = RAIZ / "index.html"
    saida.write_text(html, encoding="utf-8")
    print(f"portfólio: {saida.name} · {len(trabalhos)} trabalho(s) · "
          f"{sum(len(perfil.get(s) or []) for s in ('pesquisa', 'palestras', 'extensao', 'ensino', 'gestao'))} item(ns) nas seções")
    return saida


if __name__ == "__main__":
    main()
