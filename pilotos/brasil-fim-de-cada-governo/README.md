# Mais perto ou mais longe? As regiões do Brasil desde 2002

**Tipo:** story (piloto) · **Projeto:** eleicoes · **Status:** rascunho, no ambiente de pilotos (L0017) · **Versão:** 0.2
(2026-10-12; a 0.1, "O Brasil no fim de cada governo", usava a compilação do pesquisador)

## Pergunta
As desigualdades entre as regiões do Brasil foram reduzidas ou ampliadas desde 2002 — em quê, e quanto? (proposta 6 de
`src/propostas-roteiro.md`, escolhida pelo pesquisador em 2026-10-12, L0018).

## Dados
| Dataset | Uso |
|---|---|
| `ibge.projecao_populacao_2024` | esperança de vida, mortalidade infantil e população (2002–2024) |
| `ibge.pnadc_anual_regioes` | desocupação, Gini (2012–), renda real, analfabetismo, escolaridade (2016–), com CV |
| `ibge.pib_uf`, `ibge.inpc_mensal` | PIB por habitante em reais corrigidos |
| `bcb.salario_minimo` | salário mínimo, corrigido pelo INPC |
| `ipeadata.series_sociais` | homicídios (SIM, via Atlas da Violência) e conferências |

Mapeamento, decisões e relatório de qualidade: `src/mapeamento-dados-regionais.md` e
`projetos/eleicoes/analise/relatorio_qualidade_desigualdades_regionais.json`.

## Método e decisões (pesquisador, 2026-10-12)
D1 INPC · D2 uma série oficial por indicador · D3 cinco regiões, a do leitor em destaque · D4 período comparável mais
longo · M1 diferença e razão · M2 mais alta × mais baixa e dispersão das cinco (Williamson) · M3 margem de erro na
PNADC, limiar fixo nas demais, PIB pela razão · M4 regiões sempre relativas à população · projeção até 2024 · sem PRODES.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/ibge/consultar_regionais.py
PYTHONPATH=nucleo:. python fontes/bcb/consultar_series.py
PYTHONPATH=nucleo:. python fontes/ipeadata/consultar_series.py
PYTHONPATH=nucleo:. python projetos/eleicoes/analise/preparar_desigualdades_regionais.py
PYTHONPATH=nucleo:. python projetos/eleicoes/produtos/2026-10_brasil-fim-de-cada-governo/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/eleicoes/produtos/2026-10_brasil-fim-de-cada-governo
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Mapeamento, pipelines, contas, frases e página (2026-10-12) | Claude (Claude Code) | revisão regional pedida pelo pesquisador | narrativa e decisões de método do pesquisador; conferências automáticas sem divergência (salário mínimo × Ipea, PIB, homicídios × Atlas); revisão dos números pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
