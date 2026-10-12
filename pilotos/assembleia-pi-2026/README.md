# A nova Assembleia do Piauí

**Tipo:** story (piloto) · **Projeto:** eleicoes · **Status:** rascunho, no ambiente de pilotos (L0017) · **Deriva de:** `2026-10_forcas-politicas-pi`

## Pergunta
Como os votos para deputado estadual de 2026 viraram as 30 cadeiras da Assembleia do Piauí, e onde cada grupo é mais
forte? Piloto para testar componentes ainda não usados em produto: waffle (também em pilha), pontos conectados, tabela,
treemap aninhado, distribuição e boxplot.

## Dados
Base do produto publicado "Forças políticas no Piauí" (`data/base_forcas_pi.json.gz`, conferida com o TSE em
`analise/relatorio_qualidade_forcas_pi.json`). Nenhum dado novo.

## Método e decisões
EL0004 (grupos), EL0005 (grupo mais votado e intensidade), EL0006 (cores), EL0003 (válidos), L0015/L0016 (story
declarativo e acervo de componentes), L0017 (pilotos). Decisão local: roteiro sem revisão prévia (pesquisador,
2026-10-12).

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/eleicoes/produtos/2026-10_assembleia-pi-2026/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/eleicoes/produtos/2026-10_assembleia-pi-2026
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Roteiro, preparo dos dados e textos | Claude (Claude Code) | piloto de componentes | pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
