# Um Ponto de Cultura a cada 20 mil habitantes

**Tipo:** story · **Projeto:** cultura · **Status:** rascunho · **Versão:** 0.3 · derivado de `2026-10_pncv-cultura-viva`

## Versão 0.3 (2026-10-16)
Roteiro v4, a pedido do pesquisador: "Ponto fomentado" passa a seguir o CN0014 — fomentado pela PNAB **ou** pela Lei Paulo Gustavo (regra do canal do CN0001 nas duas políticas; valores corrigidos pelo IPCA), a definição padrão do exploratório desde 15/10/2026. Todos os números mudam (10.635 Pontos, 1,03 por 20 mil hab., 17 UFs na meta); a narrativa usa o agregado e o seletor "Fomentado por" (PNAB ou LPG · só PNAB · só LPG) entra nos cartões de exploração. Cartões novos: combinações PNAB × LPG (c1-1b) e taxa por política (c6-0). Textos marcados a conferir na página.

## Versão 0.2 (2026-10-16)
Comunicação visual revista nos quatro stories do projeto (2026-10-16): popups com os números absolutos por trás de cada % (habitantes, contemplados, R$, projetos), fatias fora do destaque com número legível, rótulos com uma casa decimal quando cabem, legenda do mapa em níveis com a escala inteira; componentes registrados na bancada (`design/padrao/bancada.yaml`). Sem mudança de roteiro nem de números.

## Pergunta
Quanto o 1º ciclo da PNAB aproximou o país da Meta 4 — um Ponto de Cultura fomentado a cada 20 mil habitantes — e o que falta, e onde?

## Dados
Só agregados da base congelada do produto de origem (`2026-10_pncv-cultura-viva/data/base.json.gz`); as bases com dados pessoais ficam em
ambiente restrito (L0004).

| Dataset | Versão | Fonte original |
|---|---|---|
| `minc.pncv_cadastro` | catálogo | ver `catalogo/datasets.yaml` |
| `minc.pnab_contemplados` | catálogo | ver `catalogo/datasets.yaml` |
| `minc.lpg_contemplados` | catálogo | ver `catalogo/datasets.yaml` |
| `minc.salic_extracoes` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.municipios` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.censo2022_municipios` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.regic_2018` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.semiarido_2022` | catálogo | ver `catalogo/datasets.yaml` |
| `ibge.amazonia_legal_2022` | catálogo | ver `catalogo/datasets.yaml` |

## Método e decisões
ADRs: L0002, L0004, L0015, L0018, CN0001, CN0003, CN0004, CN0012. Roteiro validado em 2026-10-15 (versão 2, `src/roteiro.yaml`;
prancha de leitura em `roteiro.html`). Nenhum número é escrito à mão: as frases usam marcadores preenchidos por
`src/dados_story.py`, os mesmos da prancha.

Decisões locais: definições alternativas de Ponto fomentado (só CNPJ, qualquer recebimento, por certificação, só coletivos, por documento e por faixa de valor — ≥ R$ 10, 25 e 50 mil) como recortes de leitura, pedidos pelo pesquisador; a regra oficial continua a pactuada (CN0001). Mapa por UF em classes em torno da meta (0,75 · 1 · 1,5), com a escala divergente laranja ↔ azul do DS (pesquisador, 2026-10-15).

Versão 3 do roteiro (2026-10-15, propostas aprovadas pelo pesquisador): mapa com o nível dos municípios (`analise/pncv_ampliacao.municipios_situacao`: situação pela regra pactuada, contagens de 1 a 4 Pontos sem número — L0004), c6-1 só com as três definições da frase e nota do c2-1 sem a instrução dos seletores.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/cultura/analise/preparar_pncv.py                         # base do produto de origem (restrita → agregados)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_meta4-pontos-de-cultura/src/prancha.py             # prancha do roteiro (roteiro.html)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_meta4-pontos-de-cultura/src/preparar_story.py      # viz.yaml + data/story.json
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_meta4-pontos-de-cultura         # index.html + og.png
```

## Uso de IA
O desenho do produto é do pesquisador — pergunta, briefing, recortes, decisões de método e validações —, assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos e ADRs), amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude Code (Anthropic) | ampliar o briefing e o exploratório do pesquisador em cinco caminhos de narrativa, no modelo do laboratório (L0018) | pesquisador escolheu base e enxertos |
| Roteiro e prancha | Claude Code (Anthropic) | redigir as frases (com marcadores) e os esboços da proposta escolhida | maturação conduzida pelo pesquisador: validação cartão a cartão, em rodadas, com os retrabalhos pedidos |
| Números e página | Claude Code (Anthropic) | código dos marcadores, dos dados dos cartões e da página, nos componentes do laboratório | números conferidos contra o exploratório; revisão final pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
