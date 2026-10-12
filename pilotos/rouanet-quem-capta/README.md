# Quem capta na Rouanet

**Tipo:** story (piloto) · **Projeto:** cultura (frente eixo2) · **Status:** rascunho, no ambiente de pilotos (L0017) · **Deriva de:** `2026-10_salic-rouanet`

## Pergunta
Quem capta recursos pela Lei Rouanet, e de onde são? Piloto para testar componentes ainda não usados em produto: área,
colunas empilhadas (Valores | 100%), waffle de porcentagem, pontos conectados, treemap aninhado (região → UF) e tabela.

## Dados
Só agregados da base congelada do "SALIC e Meta 2" (`data/base.json.gz`): totais por ano, trajetórias, grupos por
território (tipo, região, UF) e maiores municípios. Nenhum dado pessoal (L0004).

## Método e decisões
CN0003/CN0004 (território do proponente), CN0007 (correção pelo IPCA), CN0009 (trajetórias), L0015/L0016/L0017.
Decisão local: roteiro sem revisão prévia (pesquisador, 2026-10-12). Agrupamento das UFs nas Grandes Regiões do IBGE,
conferido com o total de cada região.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_rouanet-quem-capta/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_rouanet-quem-capta
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Roteiro, preparo dos dados e textos | Claude (Claude Code) | piloto de componentes | pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
