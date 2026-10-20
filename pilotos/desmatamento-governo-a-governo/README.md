# Desmatamento no Brasil, governo a governo

**Tipo:** story · **Projeto:** meio-ambiente · **Status:** revisão (piloto, com selo de teste) · **Versão:** 0.2 (2026-10-19), em https://cajazeiraalexandre.github.io/pilotos/desmatamento-governo-a-governo/

## Pergunta
Em quais governos o desmatamento mais subiu, em especial na Amazônia e no Cerrado? (briefing do pesquisador, 2026-10-19)

## Roteiro
Proposta 1 — O placar dos governos (`src/propostas-roteiro.md`, escolhida pelo pesquisador em 2026-10-19). Roteiro
detalhado v1 **validado** em 2026-10-19 (`src/roteiro.yaml`, prancha `roteiro.html`).

## Dados
| Dataset | Versão | Fonte original |
|---|---|---|
| `inpe.prodes_amazonia_legal_taxas` | edição 2026-10-16 | INPE, PRODES — taxa anual oficial da Amazônia Legal por UF (dashboard TerraBrasilis), 1988–2026 (2026 estimado) |
| `inpe.prodes_incrementos` | edição 2026-10-16 | INPE, PRODES Cerrado — incrementos por UF e município, 2000–2026 (bienal até 2012; 2026 estimado) |
| `mapbiomas.desmatamento_col11` | Coleção 11 | MapBiomas — desmatamento anual (perda de vegetação nativa) por bioma, UF e município, 1987–2025 |

Relatório de qualidade: `src/relatorio-qualidade.md` (números em `analise/relatorio_qualidade_desmatamento.json`).

## Método e decisões
- [MA0001](../../decisoes/MA0001-governos-e-medida-do-desmatamento.md) — governos por presidente; cada período conta
  para quem governou a maior parte dele (no PRODES, de agosto a julho, 2016 é de Dilma; no MapBiomas, ano civil, de
  Temer); FHC 2000–2002 é o ponto de partida; duas medidas: média de km² por ano no governo (ante o anterior) e
  variação de fim a fim de mandato; o PRODES 2026 entra como estimativa.
- [MA0002](../../decisoes/MA0002-tratamento-das-bases-de-desmatamento.md) — MapBiomas = perda de vegetação primária +
  secundária; MapBiomas até 2025; biênios do Cerrado contam dois anos, sem dividir o valor.
- Formato do story: L0010, L0014, L0015, L0018.

**Decisões locais:** o Explore desta edição vai até a UF (o município fica para a próxima, ver Pendências); FHC em
ocre-escuro, não cinza (cinza só para o que não é dado); PRODES Amazônia Legal e PRODES Cerrado nunca somados.
Gráficos por governo em barras, na cor do governo (barra fina = governo anterior); colunas do Cerrado na cor do
governo; quadro dos biomas em laranja (subiu) e verde-azulado (caiu), par validado com o validador da skill dataviz.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/inpe/baixar_prodes.py --biomas cerrado
PYTHONPATH=nucleo:. python fontes/inpe/padronizar_prodes.py --edicao 2026-10-16
PYTHONPATH=nucleo:. python fontes/mapbiomas/baixar_desmatamento.py
PYTHONPATH=nucleo:. python fontes/mapbiomas/padronizar_desmatamento.py
PYTHONPATH=nucleo:. python projetos/meio-ambiente/analise/qualidade_desmatamento.py
PYTHONPATH=nucleo:. python projetos/meio-ambiente/analise/desmatamento_governos.py
PYTHONPATH=nucleo:. python projetos/meio-ambiente/produtos/2026-10_desmatamento-biomas-governo/src/prancha.py
PYTHONPATH=nucleo:. python projetos/meio-ambiente/produtos/2026-10_desmatamento-biomas-governo/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/meio-ambiente/produtos/2026-10_desmatamento-biomas-governo
.venv/bin/python -m pytest tests/test_meio_ambiente_desmatamento.py
```

## Uso de IA
O desenho do produto é do pesquisador — pergunta, briefing, recortes, decisões de método e validações —, assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos e ADRs), amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Briefing | Claude (Claude Code, Anthropic) | rodada de perguntas sobre as pendências do briefing; registro em produto.yaml e MA0001 | respostas 1–7 do pesquisador, 2026-10-19 |
| Roteiro | Claude (Claude Code) | cinco propostas de roteiro (L0018) a partir do briefing; roteiro detalhado e prancha | proposta 1 escolhida e roteiro v1 validado pelo pesquisador, 2026-10-19 |
| Fontes | Claude (Claude Code) | levantamento de endereços, cobertura e tamanho (proposta-fontes.md); pipelines de download e padronização (fontes/inpe, fontes/mapbiomas) | decisões F1–F5 do pesquisador, 2026-10-19 |
| Qualidade | Claude (Claude Code) | conferência com os números oficiais do INPE e com a tabela-resumo do MapBiomas; achados Q1–Q3 | decisões Q1–Q3 do pesquisador (MA0002), 2026-10-19 |
| Dados e página | Claude (Claude Code) | analise/desmatamento_governos.py (com testes), preparo do story, textos dentro dos limites | narrativa aprovada pelo pesquisador ("Narrativa ótima"), 2026-10-19 |
| Revisão visual e piloto (0.2) | Claude (Claude Code) | colunas do Cerrado na cor do governo, cores do quadro validadas, conferência das imagens dos cartões (setas testadas e recusadas pelo pesquisador: barras mantidas); preparo para o ambiente de pilotos (L0017) | pedido do pesquisador, 2026-10-19; revisão no celular e envio pendentes |

## Pendências
- Explore por município (MapBiomas, F5): a busca do lab-viz fatia o story inteiro por cidade; um cartão de busca dentro
  de um story nacional precisa de proposta de componente.
- Revisão do pesquisador no celular; conferência externa dos números de destaque.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
