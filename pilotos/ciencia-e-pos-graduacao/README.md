# Ciência e pós-graduação no Brasil, governo a governo

**Tipo:** story · **Projeto:** ciencia-e-tecnologia · **Status:** rascunho · **Versão:** 0.1 (2026-10-15), no ambiente de pilotos

## Pergunta
O investimento público federal em pesquisa, ciência e tecnologia cresceu ao longo do tempo — em quais governos? Além
do orçamento, bolsas, programas de pós-graduação, matriculados e titulados cresceram ou não? (pergunta reformulada pelo
pesquisador em 2026-10-15)

## Roteiro
Proposta 6 (a partir da pergunta reformulada; as cinco primeiras foram recusadas), pelos governos — `src/propostas-roteiro.md`.
Roteiro detalhado v2 **validado** em 2026-10-15 (`src/roteiro.yaml`, prancha `roteiro.html`).

## Dados
| Dataset | Uso |
|---|---|
| `mcti.indicadores_cti` | investimento federal em C&T (2000–2023), execução do MCTI por unidade (2000–2024), bolsas CNPq e CAPES, pós-graduação, titulados por UF, PIB |
| `transparencia.despesa_por_orgao` | CAPES, despesa paga (2014–2025) |
| `transparencia.despesa_funcional_educacao` | CAPES por ação: bolsas de ensino superior (0487) e da educação básica (00O0) |
| `capes.bolsas_ies`, `capes.programas_pos` | bolsas e programas por estado (mapa) |
| `capes.dotacao_execucao` | conferência do orçamento da CAPES por ação (2021–2024) |
| `ibge.ipca_mensal`, `ibge.censo2022_municipios` | correção pelo IPCA (L0019); população do Censo 2022 (mapa) |

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/mcti/baixar.py
PYTHONPATH=nucleo:. python projetos/ciencia-e-tecnologia/analise/series_ct.py
PYTHONPATH=nucleo:. python projetos/ciencia-e-tecnologia/produtos/2026-10_ciencia-e-pos-graduacao/src/prancha.py
PYTHONPATH=nucleo:. python projetos/ciencia-e-tecnologia/produtos/2026-10_ciencia-e-pos-graduacao/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/ciencia-e-tecnologia/produtos/2026-10_ciencia-e-pos-graduacao
.venv/bin/python -m pytest tests/test_ciencia_ct.py
```

## Decisões locais
- Crédito reembolsável do FNDCT fora do total (D2); total oficial do MCTI com a estimativa da pós (pesquisador, 2026-10-15).
- Titulados do Amazonas e do Amapá trocados na base do MCTI e corrigidos, com aviso na legenda e na nota (2026-10-15).
- Mapa: classes em relação à média do Brasil no mesmo ano, escala marrom ↔ verde-azulado (vermelho e azul são cores de governo).

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Fontes | Claude (Claude Code, Anthropic) | levantamento (proposta-fontes.md) e relatório de cobertura | decisões F1–F5, D1–D5 do pesquisador, 2026-10-15 |
| Roteiro | Claude (Claude Code) | propostas 1–6, roteiro e prancha | proposta 6 e roteiro v2 validados pelo pesquisador, 2026-10-15 |
| Dados e página | Claude (Claude Code) | analise/series_ct.py (com testes), preparo do story, textos | conferência dos números pendente |

## Pendências
- Mapa: o roteiro promete bolsas da CAPES por instituição e cidade e programas por cidade; esta versão tem só regiões e estados.
- Revisão visual e textual do pesquisador; validação da escala do mapa.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
