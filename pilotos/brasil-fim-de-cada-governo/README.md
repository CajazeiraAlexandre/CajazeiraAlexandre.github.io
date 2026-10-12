# O Brasil no fim de cada governo

**Tipo:** story (piloto) · **Projeto:** eleicoes · **Status:** rascunho, no ambiente de pilotos (L0017)

## Pergunta
Como estavam a economia, o trabalho, a educação, a saúde e a segurança do Brasil no fim de cada governo, de 2002 ao
dado mais recente? (pesquisador, 2026-10-12: "Compare indicadores de economia, saúde e educação entre governos").

## Dados
| Dataset | Versão | Fonte original |
|---|---|---|
| `pesquisador.indicadores_governos` | v1 (2026-10-12) | compilação do pesquisador (IBGE, BCB, DataSUS, FBSP, INPE) |
| `bcb.sgs`, `ibge.pib_variacao_anual`, `ibge.ipca_mensal` | consulta | só conferência |

Conferência: `projetos/eleicoes/analise/relatorio_qualidade_indicadores_governos.json` (20 conferem, 5 com casas
cortadas, 4 divergem, 1 sem série no ano).

## Método e decisões
Ver `produto.yaml › decisoes_locais`: rótulos neutros dos retratos (2016 = ano do impeachment), valores como na
compilação (nada corrigido), Selic e reservas fora, mortalidade infantil recente sem ano fora do gráfico, componente
`serie_marcos` (experimental).

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/pesquisador/padronizar_indicadores_governos.py
PYTHONPATH=nucleo:. python projetos/eleicoes/analise/conferir_indicadores_governos.py
PYTHONPATH=nucleo:. python projetos/eleicoes/produtos/2026-10_brasil-fim-de-cada-governo/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/eleicoes/produtos/2026-10_brasil-fim-de-cada-governo
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Padronização, conferência, roteiro, textos e componente | Claude (Claude Code) | piloto com autonomia | pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
