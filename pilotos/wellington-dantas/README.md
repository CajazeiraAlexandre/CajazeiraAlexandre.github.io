# Wellington Dantas: o voto em Picos, 2012–2024 (story)

**Tipo:** story · **Projeto:** wellington-dantas · **Status:** rascunho (0.2, 2026-11-10) · **Deriva de:** `2026-11_geografia-do-voto`

## Pergunta
Como foi a trajetória de Wellington Dantas nas quatro eleições para vereador em Picos (2012–2024), em que lugares da
cidade e do interior ele é votado e quão espalhado é esse voto, em dez cartões para ver no celular.

## Cartões
capa (mapa de 2024) · trajetória (com a mediana dos outros eleitos) · Pedrinhas · o Centro de Convivência que deixou de
ser local de votação · Paraibinha · os bairros que mais votam nele · zona rural (bolhas) · saldo de 2020 para 2024 ·
concentração ("de cada 100 votos dele, quantos vieram de só 5 locais") · como os números foram feitos. Mapas sobre o
fundo de ruas da Esri; em "Opções do mapa" (recolhidas): ver como locais ou bairros; fundo OpenStreetMap, satélite ou
nenhum.

## Como foi feito
1. Briefing (2026-11-10) e cinco propostas de roteiro (`src/propostas-roteiro.md`); escolha: proposta 2, com a capa da
   1 e o cartão de Pedrinhas da 4 (L0018).
2. Roteiro detalhado (`src/roteiro.yaml`) e prancha de leitura (`roteiro.html`); validado em 2026-11-10 (v2).
3. Página própria em cartões (decisão do pesquisador), montada por `src/preparar_story.py` a partir da base do
   exploratório (todo número em Python; L0002). Imagens 9:16 em `imagens/`.

```bash
python projetos/wellington-dantas/analise/geografia_voto.py          # base do exploratório
python projetos/wellington-dantas/produtos/2026-11_trajetoria-story/src/prancha.py
python projetos/wellington-dantas/produtos/2026-11_trajetoria-story/src/preparar_story.py
python projetos/wellington-dantas/produtos/2026-11_trajetoria-story/src/imagens.py   # imagens 9:16
```

## Decisões
EL0003, EL0009 e WD0001 (provisórias, nota no último cartão). Locais deste produto: mediana dos votos dos outros
eleitos de cada eleição, sem ligar pessoas (M1, pesquisador); R1 fundo de ruas, R4 quedas ≥ 10 votos, R5 "povoados
urbanizados", R6 imagens: recomendações aplicadas por padrão.

## Uso de IA
A ideia do story, o público (o vereador, no celular), o tamanho, a voz, a exclusão de outros vereadores, a escolha do
roteiro, a validação cartão a cartão e os pedidos de ajuste (mediana dos outros eleitos, formas do mapa, bolhas na zona
rural, texto de Pedrinhas) são do pesquisador; o formato de propostas e de roteiro (L0018) e a base conferida são do
laboratório (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas e roteiro | Claude (Claude Code, Anthropic) | Cinco propostas, roteiro e prancha com números da base | Pesquisador escolheu e validou (2026-11-10) |
| Conferência | Claude | Mudança das seções do Centro de Convivência para a escola José João de Moura (cadastro do TSE) | Pendente: revisão do story |
| Página e imagens | Claude | Página em cartões, mapas e imagens 9:16 | Pendente: revisão do story |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
