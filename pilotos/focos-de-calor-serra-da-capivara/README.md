# Onde o fogo se concentra no Território Serra da Capivara

**Tipo:** visualizacao · **Projeto:** rio-piaui · **Status:** rascunho (v0.3, 2026-11-07)

## Pergunta
Onde os focos de calor se concentram no Território Serra da Capivara em cada ano de 2003 a 2025, e como essas manchas
mudam de um ano para o outro?

O leitor escolhe o ano na régua, sobre um mapa de fundo que pode aproximar e mover a qualquer momento, inclusive
durante a animação. O fundo pode ser claro, escuro, detalhado, satélite ou relevo. Em ⇄ Explorar ficam:
- o que ver (faixas do MSKDE, focos ou os dois);
- o número de faixas: três, ou uma faixa só (acima do p80, do p90 ou do p95), com um único conjunto de polígonos por
  ano, também na animação;
- o raio do MSKDE (2, 3, 5 ou 8 km);
- os limites das faixas (iguais nos 23 anos ou de cada ano);
- a versão da animação.

▶ anima a série com a interpolação entre conjuntos de polígonos, em três versões escolhidas num seletor: Artigo, Com
ajustes e Campos de distância.

## Dados
| Dataset | Uso | Fonte original |
|---|---|---|
| `inpe.queimadas_focos` | focos do satélite de referência, 2003–2025 | INPE, Programa Queimadas |
| `pi.territorios_desenvolvimento` | os 18 municípios do território | SEPLAN-PI |
| `ibge.malha_municipios_2022` | limites municipais | IBGE |
| `ana.bho_hidrografia` | curso do Rio Piauí | ANA, BHO |
| `icmbio.unidades_conservacao` | parques nacionais da Serra da Capivara e da Serra das Confusões | ICMBio, CNUC |

## Método e decisões
- **MR0003 (MSKDE):** faixas de densidade por ano com os parâmetros de `analise/mskde_focos.yaml`, cada um com o porquê.
  O pesquisador os aprovou em 2026-11-07: raio de 5 km, células de 250 m, margem de 5 km e percentis 80/90/95 com
  limites comuns aos 23 anos. Referência: Queiroz Neto, Santos e Vidal, SIBGRAPI 2016, DOI 10.1109/SIBGRAPI.2016.049.
- **MR0001 (interpolação):** recurso do artigo de Ramos, Santos e Cavalcante Neto (SIBGRAPI 2019, DOI
  10.1109/SIBGRAPI.2019.00027). Roda no navegador, como na página do recurso (D6), e entra na página sem cópia à mão:
  `analise/gerar_focos_mskde.py` monta `src/extensao.js`. Buracos ficam fora da animação (D4, em aberto).
- **Alternativas do MSKDE (pesquisador, 2026-11-07, "Raio e escopo"):** 8 variantes calculadas em Python
  (`analise/mskde_focos_variantes.py`), com o porquê de cada valor em `analise/mskde_focos_variantes.yaml`. A de
  5 km com limites comuns é idêntica à aprovada (teste); as outras servem para comparar.
- **Faixa única (pesquisador, 2026-11-07):** é a região acima do limite escolhido. Ela é igual, ano a ano, ao MSKDE
  rodado com um nível só (conferido em `analise/mskde_focos_variantes.py`). Usa a cor daquele limite na escala.
- **Cores (pesquisador, 2026-11-07):** faixas numa escala de fogo, laranja → vermelho, em brasa no tema escuro;
  focos em violeta com anel; rio em azul; parques nacionais em verde tracejado. A escala foi conferida pelo validador
  de paleta da skill dataviz. Verde × vermelho fica abaixo do piso para daltonismo: os parques têm, por isso,
  tracejado e nome.
- **Regiões encaixadas (pesquisador, 2026-11-07):** a animação interpola, cada uma como um conjunto, as regiões acima
  de p80, de p90 e de p95, e as empilha. Nas regiões desenhadas há 3 buracos; nas faixas soltas seriam 496.
- **L0002, L0007, L0012:** a base é toda feita em Python; a página só escolhe e desenha (a animação é a exceção da
  MR0001). A especificação é declarativa, e no celular a altura é livre.
- **Decisões locais (do assistente, a revisar):**
  - tons exatos das cores;
  - fundo inicial claro (escuro no tema escuro);
  - animação calculada no quadro de áreas iguais da MR0001 D7 e levada ao mapa;
  - a imagem do ↗ Baixar sai sem fundo;
  - ano inicial 2025;
  - ritmo da animação: 1,5 s de transição e 0,5 s de parada por ano;
  - contornos simplificados em 125 m, só no desenho.

## Como reproduzir
```bash
# a partir da raiz do laboratório
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/mskde_focos.py          # faixas do MSKDE + relatório
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/mskde_focos_variantes.py # variantes do ⇄ Explorar (~3 min)
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/preparar_focos_mskde.py # data/base.json
PYTHONPATH=nucleo:. python projetos/rio-piaui/analise/gerar_focos_mskde.py    # src/extensao.js + index.html
pytest tests/test_rio_piaui_focos_mskde.py tests/test_rio_piaui_mskde.py tests/test_metodos_mskde.py
```

## Pendências
- Revisão do pesquisador.
- Exportação: o exportador ainda não alcança recursos de outro projeto (MR0001, MR0003, `mskde.py`, `interpolacao.js`,
  `campos.js`). Antes de publicar, há duas saídas, a decidir pelo pesquisador: promover os recursos (ADR) ou dar ao
  exportador suporte a esses arquivos.

## Uso de IA
São do pesquisador:
- a pergunta, o briefing e o recorte do projeto;
- a ideia de trazer o MSKDE ao laboratório e a aprovação dos seus parâmetros;
- as escolhas da peça: camadas, ano, animação nas três versões e regiões encaixadas;
- o método de interpolação, que é o do seu artigo de 2019.

Os modelos e as especificações do laboratório foram amadurecidos por ele com apoio dos agentes. A tabela registra o que
a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a
IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Recurso MSKDE | Claude (Claude Code, Anthropic) | implementar o método a partir do artigo, com testes (MR0003) | parâmetros aprovados em 2026-11-07; D4–D6 a revisar |
| Variantes do MSKDE | Claude (Claude Code) | raio × limites pedidos pelo pesquisador, com o porquê de cada valor | a fazer, na revisão |
| Base da página | Claude (Claude Code) | regiões encaixadas, focos, contexto e números em `data/base.json` | a fazer, na revisão |
| Componente, cores e textos | Claude (Claude Code) | mapa com fundo, escala de fogo validada, componente, textos e testes no Chrome sem interface | a fazer, na revisão |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
