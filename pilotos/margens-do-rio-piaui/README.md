# As margens do Rio Piauí: uso do solo, desmatamento e fogo

**Tipo:** narrativa (peça de rolagem com mapa) · **Projeto:** rio-piaui · **Status:** rascunho v0.1 (2026-11-06) · nos pilotos em 2026-11-07:
https://cajazeiraalexandre.github.io/pilotos/margens-do-rio-piaui/ (versão de teste, fora dos buscadores)

## Pergunta
Apresentar sobre o mapa, no entorno de 5 km do Rio Piauí no Território Serra da Capivara, os indicadores do
exploratório `2026-11_leito-rio-piaui`: uso do solo (2021), desmatamento (PRODES até 2000 e por período; alertas) e
fogo (focos e área queimada). Peça de ensaio: o pesquisador está testando recursos e formas de narrativa e pediu ao
assistente um roteiro próprio (`src/roteiro.md`), dispensando as propostas da L0018.

## Dados
Os mesmos do exploratório (ver `produto.yaml`): ANA BHO 2017, IBGE 2022, CNUC 2025_08, ESA WorldCover 2021,
PRODES Caatinga (polígonos, 2026-11-06), MapBiomas Alerta (2026-10-15), INPE focos (2003–2025) e AQ1km (2002–2025).

## Método e decisões
- RP0001, RP0002, MR0002, MA0002, L0002, L0003 (resumos no bloco de metodologia da página).
- Camadas: uso do solo e PRODES como imagens de ~50 m na faixa de 5 km (`analise/story_margens.py`); focos e alertas
  como vetores; faixas, rio e parques da peça "Navegando".
- Destaques calculados: cada passo "onde" vai ao município atravessado com o maior valor do indicador
  (`{max: chave}` em `src/passos.yaml`, resolvido por `analise/gerar_margens.py`). Resolução gravada em
  `src/passos-resolvidos.json`.
- Textos com marcadores `{{caminho|formato}}` preenchidos de `data/indicadores.json`; nenhum número à mão.

### Decisões locais
- Nos pilotos (2026-11-07): prévia do link = mapa no passo "uso do solo"; no celular, a linha técnica "Fundo · zoom" só
  aparece quando o fundo falha (cobria o seletor e a legenda).
- Doze passos em três atos (uso do solo, desmatamento, fogo), do todo (faixa inteira) ao detalhe (trecho do rio num
  município). Fundo padrão OpenFreeMap claro; satélite no seletor.
- Classes de período do PRODES na imagem: até 2000, 2001–2012, 2013–2019, 2020–2025 (os períodos bienais caem
  inteiros numa classe).
- O passo 4 fala da água, não da "cidade": área construída e solo exposto não passam de 1 % do anel de 100 m em
  nenhum município.

**Publicação nos pilotos (pesquisador, 2026-11-07):** endereço `pilotos/margens-do-rio-piaui/`, com selo
"Versão de teste", aviso de produto em testes e prévia do link (og.png). A página carrega o MapLibre, o Scrollama, o d3
e os fundos de mapa da internet; os dados estão todos dentro dela.

**Gestos no celular (pesquisador, 2026-11-06):** gestos cooperativos do MapLibre — um dedo rola a narrativa, dois dedos movem o mapa, Ctrl + rolagem aproxima no computador; toque em polígono ou ponto continua abrindo a ficha.

## Como reproduzir
```bash
# bases e exploratório conforme o README de 2026-11_leito-rio-piaui; depois:
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/story_margens.py    # data/: imagens, vetores, indicadores
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/gerar_margens.py    # index.html
PYTHONPATH=nucleo:. python -m pytest -q tests/test_rio_piaui_margens.py
# pilotos (L0017): selo, aviso e prévia do link saem de produto.yaml › versao e publicacao; og.png = mapa no passo
# "uso do solo" sem os cartões (1200 × 630). Depois:
PYTHONPATH=nucleo:. python ferramentas/publicar_pilotos.py --so 2026-11_margens-rio-piaui
```

## Uso de IA
O pedido, o recorte, as bases e as decisões de método são do pesquisador, assim como o recurso (MR0002), os
componentes e os modelos do laboratório, amadurecidos por ele com apoio dos agentes. A pedido dele, para esta peça de
ensaio, o assistente redigiu o roteiro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador
e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Roteiro em três atos e textos dos cartões (`src/roteiro.md`, `src/passos.yaml`) | Claude (Claude Code, Anthropic) | proposta de narrativa para teste do recurso | revisão do pesquisador pendente |
| Camadas (imagens de uso do solo e PRODES, vetores) e indicadores por município (`story_margens.py`) | Claude | levar os indicadores do exploratório ao mapa | números testados contra `indicadores.json`; conferência do pesquisador |
| Gerador com destaques calculados e marcadores (`gerar_margens.py`), código da peça, testes | Claude | página autocontida e reproduzível | testes automatizados; revisão na tela pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
