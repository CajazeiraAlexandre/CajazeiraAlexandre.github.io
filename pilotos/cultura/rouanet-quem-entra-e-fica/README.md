# Quem entra e quem fica na Lei Rouanet

**Tipo:** story · **Projeto:** cultura · **Status:** rascunho · **Versão:** 0.5 · derivado de `2026-10_salic-rouanet`

## Versão 0.5 (2026-10-16)
Comunicação visual revista nos quatro stories do projeto (2026-10-16): popups com os números absolutos por trás de cada % (habitantes, contemplados, R$, projetos), fatias fora do destaque com número legível, rótulos com uma casa decimal quando cabem, legenda do mapa em níveis com a escala inteira; componentes registrados na bancada (`design/padrao/bancada.yaml`). Sem mudança de roteiro nem de números.

## Pergunta
Quantos proponentes captam pela primeira vez na Lei Rouanet a cada ano, onde eles estão e quantos conseguem captar de novo?

## Dados
Só agregados da base congelada do produto de origem (`2026-10_salic-rouanet/data/base.json.gz`); as bases com dados pessoais ficam em
ambiente restrito (L0004).

| Dataset | Versão | Fonte original |
|---|---|---|
| `minc.salic_extracoes` | catálogo | ver `catalogo/datasets.yaml` |
| `minc.pnab_contemplados` | catálogo | ver `catalogo/datasets.yaml` |
| `minc.lpg_contemplados` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.municipios` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.regic_2018` | catálogo | ver `catalogo/datasets.yaml` |

## Método e decisões
ADRs: L0002, L0004, L0015, L0018, CN0007, CN0009. Roteiro validado em 2026-10-15 (versão 1, `src/roteiro.yaml`;
prancha de leitura em `roteiro.html`). Nenhum número é escrito à mão: as frases usam marcadores preenchidos por
`src/dados_story.py`, os mesmos da prancha.

Decisões locais: médias das coortes de 2016 a 2020 ponderadas pelos novos de cada coorte; no Explorar, anos alternados da série; caminhos suprimidos (1 a 4 proponentes) fora das somas das trajetórias, como no exploratório.

Versão 2 do roteiro (2026-10-15, propostas aprovadas pelo pesquisador): valor captado pelos novos (conta nova, `analise/salic_indicadores.valor_por_entrada`, com supressão de situações com 1 a 4 proponentes no ano; os totais por ano conferem com os do exploratório) e nota sobre o bloco cinza do Sankey.

Versão 0.2 (2026-10-15, pedido do pesquisador: “os três primeiros cartões exploram o mesmo gráfico”): roteiro v3 — Quem chega com números grandes, colunas (Valores | 100%) e duas barras de proponentes × valor; mapa região → UF (conta nova `analise/salic_indicadores.entradas_por_uf`, com supressão de 1 a 4) para a parte de novos e a parte que não voltou; waffle “de cada 100 novos”; caminhos do fomento direto; Explorar em colunas por território.

Versão 0.3 (2026-10-15, pedido do pesquisador): “contínuo” passa a se chamar permanência; capítulo “Com quanto e para onde” — faixa do valor captado no ano por situação, retorno dos novos pela faixa do primeiro ano (`analise/salic_indicadores.situacao_por_faixa`) e local de execução por situação (`analise/salic_execucao.execucao_por_situacao`), contas novas com supressão de 1 a 4; cores com sentido fixo pelos papéis do DS (primeira vez = laranja, permanência = verde, não voltou = cinza, fomento direto = azul) e dicas com os números absolutos.

Versão 0.4 (2026-10-15, pedido do pesquisador: cartões 6, 8, 10 e 12): retorno acumulado em colunas (1, 2, 3 e 5 anos e até 2025), entrada × saída por território em pontos conectados, voltou × não voltou por faixa do primeiro ano e entrantes × toda a rede no fomento direto (conta nova `analise/salic_indicadores.fomento_federal_por_situacao`).

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/cultura/analise/preparar_salic.py                         # base do produto de origem (restrita → agregados)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_rouanet-quem-entra-e-fica/src/prancha.py             # prancha do roteiro (roteiro.html)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_rouanet-quem-entra-e-fica/src/preparar_story.py      # viz.yaml + data/story.json
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_rouanet-quem-entra-e-fica         # index.html + og.png
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude Code (Anthropic) | cinco ideias de narrativa a partir do exploratório | pesquisador escolheu base e enxertos |
| Roteiro e prancha | Claude Code (Anthropic) | redação das frases (com marcadores) e esboços | pesquisador validou cartão a cartão |
| Números e página | Claude Code (Anthropic) | código dos marcadores, dos dados dos cartões e da página | números conferidos contra o exploratório; revisão final pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
