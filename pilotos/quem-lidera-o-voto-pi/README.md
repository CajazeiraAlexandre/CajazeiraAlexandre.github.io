# Quem lidera o voto no Piauí

**Tipo:** story · **Projeto:** eleições · **Status:** rascunho · **Deriva de:** `2026-10_forcas-politicas-pi`

## Pergunta
Quem lidera o voto no Piauí em 2026, como isso se compara às prefeituras de 2024 e o que mudou desde 2022 — por
município e por Território de Desenvolvimento.

## Formato
Story declarativo (L0015): capa + 6 capítulos e 19 cartões, descritos em `viz.yaml` e desenhados pelo renderizador
comum (`web/componentes/lab-viz.js`). Os mapas usam o `Lab.mapa` do design system (L0006: câmera por cartão, fundo
vetorial, referência e cidades); o mesmo mapa segue de um cartão para o outro mudando cor, forma (mapa → bolhas → mapa)
e câmera, e o mesmo Sankey é montado em fases (blocos de 2022, de 2026, faixas). Seletores no texto do cartão: grupo,
território e município (mapa realçado + barras de 2026 com a fina de 2022). `#cartao=c3-3` abre num cartão.

Versão 0.1 (10/10/2026): página escrita à mão (`src/legado/`), substituída em 12/10/2026 pela migração para o
declarativo, por decisão do pesquisador; o roteiro validado (v5) não mudou.

## Dados
Mesma base do produto de origem (`../2026-10_forcas-politicas-pi/data/base_forcas_pi.json.gz`, gerada por
`analise/forcas_pi.py`) e os contornos da malha municipal do IBGE 2022 (`analise/html_forcas_pi.contornos`). Datasets:
ver `produto.yaml`. O recorte do story fica em `data/base.json.gz`.

## Método e decisões
ADRs: L0001, L0002, L0003, L0006, EL0002, EL0003, EL0004, EL0005, EL0006. Grupos com os nomes do produto de origem:
PT/PV/PCdoB, PSD, MDB, União Progressista (PP + União Brasil) e Outros.

**Decisões locais (só deste produto)** — também em `produto.yaml › decisoes_locais`:
- *Roteiro antes do produto:* `src/roteiro.yaml` validado pelo pesquisador em 10/10/2026 (versão 5, após cinco
  rodadas); o gerador recusa roteiro não validado. Prancha de leitura: `roteiro.html` (`src/prancha.py`).
- *Indicadores aprovados:* % dos votos válidos do estado nos municípios em que o grupo lidera; municípios com prefeito
  (2024) do grupo mais votado para deputado estadual (2026).
- *Mapas no `Lab.mapa` do design system* (L0006, modo compacto): câmera por cartão no roteiro (`camera`), zoom
  + − ⟲, card ao tocar, referência (UFs vizinhas e cidades do IBGE — `labdados.mapa`) e fundo vetorial OpenFreeMap
  (sem internet, o mapa aparece sem o fundo). Para ajustar um enquadramento: abrir com `?editar=1`, enquadrar, "Copiar
  câmera" e colar no `src/roteiro.yaml` (não exige nova validação). Substitui o mapa próprio com fundo do
  OpenStreetMap, bloqueado em páginas abertas por arquivo.
- *Bolhas em escala fiel* no cartão c1-4 (`escala_bolhas: fiel`, exceção prevista na L0006): a área é sempre
  proporcional aos votos, inclusive Teresina — o cartão fala justamente do peso de Teresina (21,8% dos votos).
- *Palcos de barras e Sankey* desenhados no `app.js` (estados e transições entre cartões); o motor do story é o mesmo
  do piloto (`projetos/cultura/produtos/2026-10_rouanet-onde-acontece`); a promoção para `web/componentes/` fica para
  depois, com ADR.
- *Perdas por grupo:* o Explorar começa pelo PT/PV/PCdoB e segue a ordem fixa do EL0006 (não o ranking de perdas).
- *Prefeito:* nome de urna como registrado no TSE (em maiúsculas).

## Como reproduzir
```bash
# a partir da raiz do laboratório
python projetos/eleicoes/produtos/2026-10_quem-lidera-o-voto-pi/src/prancha.py                       # prancha do roteiro
PYTHONPATH=nucleo:. python projetos/eleicoes/produtos/2026-10_quem-lidera-o-voto-pi/src/preparar_story.py   # data/story.json
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/eleicoes/produtos/2026-10_quem-lidera-o-voto-pi     # index.html e og.png
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Roteiro | Claude Code (Claude Opus 5.5, Anthropic) | rascunho dos capítulos e frases a partir do "Forças políticas no Piauí" | cinco rodadas de comentários; validado pelo pesquisador (10/10/2026) |
| Código | Claude Code | `prancha.py`, `preparar.py`, `app.js`, modelo HTML | revisão do produto pelo pesquisador (pendente) |
| Migração (12/10/2026) | Claude Code | `preparar_story.py`, `viz.yaml` e extensões do renderizador comum (mapa e Sankey em estado entre cartões, pilha mapa + barras) | revisão do story no celular pelo pesquisador (pendente) |
| Números | — | nenhum número digitado: frases, tabelas e contagens preenchidas por código a partir da base | conferência na prancha (tabela de marcadores) |

Portaria CNPq nº 2.664/2026. A responsabilidade pelo conteúdo é do pesquisador; a IA não é autora.

## Licença
Código: MIT · Dados derivados: CC BY 4.0 · Fundo dos mapas: © OpenFreeMap · © colaboradores do OpenStreetMap (ODbL)
