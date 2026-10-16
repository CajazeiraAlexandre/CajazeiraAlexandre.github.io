# Onde a Rouanet acontece

**Tipo:** story (piloto do tipo) · **Projeto:** cultura (frente eixo2) · **Status:** rascunho · **Deriva de:** `2026-10_salic-rouanet` (seções 5 e 12)

## Versão 0.4 (2026-10-16)
Comunicação visual revista nos quatro stories do projeto (2026-10-16): popups com os números absolutos por trás de cada % (habitantes, contemplados, R$, projetos), fatias fora do destaque com número legível, rótulos com uma casa decimal quando cabem, legenda do mapa em níveis com a escala inteira; componentes registrados na bancada (`design/padrao/bancada.yaml`). Sem mudança de roteiro nem de números.

## Versão 0.3 (2026-10-15)
Roteiro v4, validado pelo pesquisador em 15/10/2026 (`src/roteiro.yaml`; prancha em `roteiro.html`): a concentração em
cada etapa — a régua e a série 2016–2025, do aprovado ao captado (com o Sankey do funil), quem capta, **dentro das
cidades** (setores censitários, favelas e comunidades urbanas, periferias metropolitanas e as limitações), onde acontece
(Sankeys da sede para a execução, por tipo de município e por região) e o que acompanhar (Meta 2). Execução 2019–2025.
Pergunta: em que etapas o recurso da Lei Rouanet se concentra — e em qual ele começa a se espalhar?

Gerada pelo gerador comum do projeto (`analise/story_produto.py`): `src/preparar_story.py` escreve `viz.yaml` e
`data/story.json` a partir do roteiro e de `src/dados_story.py` (os mesmos marcadores da prancha). A versão 0.2 fica em
`src/legado/` (`viz_v02.yaml`, `story_v02.json`, `preparar_story_v02.py`); a página 0.2 tem cópia local fora do git.

O texto abaixo descreve a versão 0.2.

## Pergunta (0.2)
Quando um projeto da Lei Rouanet é realizado fora da cidade de quem o propôs, o recurso se espalha pelo país?
(Meta 2 do PNC — desconcentração do fomento indireto.)

## Formato
Story declarativo (L0015): capa + 6 capítulos e 17 cartões que se passam para o lado, descritos em `viz.yaml` e
desenhados pelo renderizador comum (`web/componentes/lab-viz.js`) — o mesmo do story "2º turno na sua cidade". Cada
cartão tem o seu componente com dados prontos do Python (barras 100%, Sankey, números grandes); quando dois cartões
seguidos usam o mesmo componente, as marcas mudam de estado em vez de serem redesenhadas. Os cartões de Explore têm o
seletor no próprio texto (agrupamento; UF). "Como ler", "Notas e fontes" (com a metodologia) e "Baixar ou Compartilhar"
(imagem 9:16 de cada cartão) ficam na barra do pé. `#cartao=c3-2` abre num cartão.

Versão 0.1 (10/10/2026): página escrita à mão (`src/legado/`), substituída em 12/10/2026 pela migração para o
declarativo, por decisão do pesquisador; o roteiro validado (v1) não mudou.

## Dados
| Dataset | Uso |
|---|---|
| `minc.salic_extracoes` | aportes (valor captado), incentivadores e cadastro de proponentes |
| `minc.salic_api` | municípios de realização por PRONAC (consulta de 09/10/2026) |
| `ibge.municipios`, `ibge.censo2022_municipios`, `ibge.regic_2018` | população, capital, arranjo da capital, porte, hierarquia urbana |

Os números vêm da seção `execucao` da base congelada do produto de origem
(`../2026-10_salic-rouanet/data/base.json.gz`); o recorte do story fica em `data/base.json.gz`.

## Método e decisões
ADRs: L0002, L0003, L0004, CN0003, CN0004, CN0007, CN0009, CN0010. Universo único: projetos com PRONAC de 2021 a 2025
que captaram (13.619; R$ 11,3 bilhões nominais); local de realização declarado; valor de projetos com vários municípios
dividido igualmente (provisório — CN0010).

**Decisões locais (só deste produto):**
- *Roteiro antes do produto:* `src/roteiro.yaml` validado pelo pesquisador em 10/10/2026 (versão 1); o gerador recusa
  roteiro não validado. A prancha de leitura (`roteiro.html`, por `src/prancha.py`) é a peça de revisão.
- *Nenhum número no roteiro:* as frases usam marcadores preenchidos pelo Python; a conferência marcador → valor →
  origem está no fim da prancha. Porcentagens dos gráficos e das frases do Explore também vêm prontas do Python;
  o arredondamento para exibição foi conferido (490 porcentagens, nenhuma divergência Python × navegador).
- *Palcos próprios do story:* barras 100% e Sankey vertical desenhados no `app.js` (mesmas regras do catálogo:
  ordem e cor fixas das categorias, Sankey vertical), em vez de `Lab.linhaBarra100`/`Lab.sankey`, para permitir os
  estados e as transições entre cartões. Se o piloto for aprovado, a promoção para `web/componentes/` vira proposta com ADR.

## Como reproduzir
```bash
# a partir da raiz do laboratório
python projetos/cultura/produtos/2026-10_rouanet-onde-acontece/src/prancha.py                       # prancha do roteiro
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_rouanet-onde-acontece/src/preparar_story.py   # data/story.json
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_rouanet-onde-acontece     # index.html e og.png
```
A base de origem é gerada por `projetos/cultura/analise/preparar_salic.py` (ver o README do produto SALIC).

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Proposta do formato | Claude Code (Claude Opus 5.5, Anthropic) | estrutura de design e interação do tipo story | duas rodadas de comentários; aprovada pelo pesquisador (10/10/2026) |
| Roteiro | Claude Code | rascunho dos capítulos e frases a partir das seções 5 e 12 do produto SALIC | roteiro lido na prancha e validado pelo pesquisador (10/10/2026) |
| Código | Claude Code | `prancha.py`, `preparar.py`, `app.js`, modelo HTML | revisão do protótipo pelo pesquisador (pendente) |
| Migração (12/10/2026) | Claude Code | `preparar_story.py`, `viz.yaml` e extensões do renderizador comum (base única, seletor no cartão, estado entre cartões) | revisão do story no celular pelo pesquisador (pendente) |
| Números | — | nenhum número digitado: todos preenchidos por código a partir da base | conferência na prancha (tabela de marcadores) |

Portaria CNPq nº 2.664/2026. A responsabilidade pelo conteúdo é do pesquisador.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
