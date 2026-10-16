# A Lei Paulo Gustavo chegou a todo o país; o dinheiro, nem tanto

**Tipo:** story · **Projeto:** cultura · **Status:** rascunho · **Versão:** 0.2 · derivado de `2026-10_lpg-exploratorio`

## Versão 0.2 (2026-10-16)
Comunicação visual revista nos quatro stories do projeto (2026-10-16): popups com os números absolutos por trás de cada % (habitantes, contemplados, R$, projetos), fatias fora do destaque com número legível, rótulos com uma casa decimal quando cabem, legenda do mapa em níveis com a escala inteira; componentes registrados na bancada (`design/padrao/bancada.yaml`). Sem mudança de roteiro nem de números.

## Pergunta
O fomento direto descentralizado da Lei Paulo Gustavo espalhou o recurso pelo território ou só os contemplados?

## Dados
Só agregados da base congelada do produto de origem (`2026-10_lpg-exploratorio/data/base.json.gz`); as bases com dados pessoais ficam em
ambiente restrito (L0004).

| Dataset | Versão | Fonte original |
|---|---|---|
| `minc.lpg_contemplados` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.municipios` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.censo2022_municipios` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.semiarido_2022` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.amazonia_legal_2022` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.regic_2018` | catálogo | ver `catalogo/datasets.yaml` |

## Método e decisões
ADRs: L0002, L0004, L0015, L0018, CN0002, CN0003, CN0012. Roteiro validado em 2026-10-15 (versão 2, `src/roteiro.yaml`;
prancha de leitura em `roteiro.html`). Nenhum número é escrito à mão: as frases usam marcadores preenchidos por
`src/dados_story.py`, os mesmos da prancha.

Decisões locais: capital × região metropolitana × interior pela classificação da própria base da LPG; a população de cada grupo soma os municípios classificados, e os 472 municípios sem contemplado (1,2% da população) ficam num grupo à parte, sem atribuição (pesquisador, 2026-10-15).

Versão 3 do roteiro (2026-10-15, propostas aprovadas pelo pesquisador): mapa região → UF → município com cores em relação à média do Brasil (75% · 100% · 125%; "nenhum contemplado" à parte; municípios com 1 a 4 contemplados em hachura), Sankey de quem pagou para onde mora (destino capital × região metropolitana × interior acrescentado a `analise/lpg_fluxos.py`) e frase do Explorar comparando a fatia do valor com a da população.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/cultura/analise/preparar_lpg.py                         # base do produto de origem (restrita → agregados)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_lpg-onde-chegou/src/prancha.py             # prancha do roteiro (roteiro.html)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_lpg-onde-chegou/src/preparar_story.py      # viz.yaml + data/story.json
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_lpg-onde-chegou         # index.html + og.png
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude Code (Anthropic) | cinco ideias de narrativa a partir do exploratório | pesquisador escolheu base e enxertos |
| Roteiro e prancha | Claude Code (Anthropic) | redação das frases (com marcadores) e esboços | pesquisador validou cartão a cartão |
| Números e página | Claude Code (Anthropic) | código dos marcadores, dos dados dos cartões e da página | números conferidos contra o exploratório; revisão final pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
