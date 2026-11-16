# Contando histórias a partir de dados: visualização de dados

**Tipo:** didatico · **Projeto:** dataviz-didatico · **Status:** rascunho (piloto 0.4 em validação) · **Página (IFPI 2026.2):** https://cajazeiraalexandre.github.io/ifpi-2026-2/visualizacao-de-dados/

## Pergunta
Por que visualizar dados, como um gráfico é construído (marcas, canais e atributos) e como escolhê-lo pela tarefa
perceptiva do leitor — comparar, parte/todo, tendência temporal, distribuição e correlação, observação ampla —, com
as ferramentas disponíveis. Terceiro material da série da disciplina (Tópicos Especiais; graduação em Tecnologia em
Sistemas para Internet, IFPI), a partir dos slides "Contando histórias a partir de dados — Visualização". Sem Parte
III (desafios) nesta primeira versão (pesquisador, 2026-11-07).

## Estrutura
- **Parte I · Conceitos** (`src/parte1.yaml`), em sete temas, na ordem dos slides revistos da aula (piloto 0.4,
  2026-11-10): **o que é visualizar** (um gráfico é uma tradução; a visualização em todo o fluxo; descobrir ×
  comunicar); **por que visualizar** (Nørretranders desenhado, atributos pré-atentivos com um teste interativo, a forma
  que a tabela esconde, quarteto de Anscombe); **visualizar também pode confundir** (as quatro armadilhas e outras
  quatro, em figuras); **marcas e canais** (marcas, canais, ordem de eficácia, figura de expressividade e eficácia,
  esquemas A–D, receita de quatro passos aplicada a um gráfico do professor); **cor e acabamento** (anatomia de um
  gráfico completo, três tipos de paleta, cor para todos com a simulação de deuteranopia); **tarefas perceptivas, uma
  a uma** (navegação 1–5 com os gráficos do professor no DATADOC/OP+ e o que reparar em cada um; “Qual é a tarefa?”
  com quatro gráficos e a resposta recolhida); **ferramentas e síntese** (da hipótese ao gráfico). Cada tema termina
  com o link para o slide correspondente (`slides.html#N`). Complementos do assistente marcados com `c: true`.
- **Parte II · Aplicações** (`src/app.js`), demonstrações cadenciadas na ordem da aula, com dados públicos reais —
  cada aplicação é uma sequência de passos que troca o gráfico no lugar, com um texto por passo: 1 **Da tabela ao
  gráfico**; 2 **As armadilhas** (IPCA da TV → eixo em zero → contexto 1995–2025; pizza de 27 fatias → barras); 3 **Os
  esquemas A–D com dados reais**, mais um construtor recolhido; 4 **Do enfeite ao gráfico completo** (com enfeites →
  sem enfeites → o que falta → anatomia completa); 5 **A cor segue o dado** (categórica → sequencial → divergente → cor
  para todos); 6–10 **uma aplicação por tarefa perceptiva** (a de tendência começa pela tabela de dezembros); 11 **A
  tarefa de cada gráfico** (galeria explicada). Sem testes nem jogo (revisão do professor, 2026-11-07).
- **Parte III · Atividade** (`src/parte3.yaml` e `src/app.js › ATIVIDADES`, 2026-11-10): cinco hipóteses, uma por tarefa
  perceptiva, com dados do material — alfabetização nos territórios do Piauí (comparar), as três maiores UFs no
  eleitorado (parte/todo), a inflação de 1995 a 2025 (tendência), Bolsa Família × alfabetização no Piauí (correlação) e
  a rede privada nas matrículas por UF (observação ampla). Em cada uma, três escolhas — tarefa, gráfico, canais —, com o
  gráfico desenhado e um comentário a cada escolha, sem placar, e a solução comentada recolhida. Depois, a
  **recapitulação** com as 20 hipóteses do Laboratório de hipóteses (tarefa, gráfico e canais recolhidos) e o **Agora
  você** (a atividade dos slides, com a síntese e um exemplo preenchido).
- **Apoio** (`src/referencias.yaml`): objetivos, autoria, uso de IA, slides, referências, bases (onde e como baixar),
  CSVs, materiais anteriores, como citar.
- **Slides** (`slides.html`, 2026-11-09): versão HTML revista dos slides da aula, conforme a revisão em
  `projetos/dataviz-didatico/docs/2026-11-09_revisao-slides-visualizacao.md` — 51 slides em cinco partes (desde 2026-11-09 com a visualização em todo o fluxo, exploratória × explicativa,
  anatomia de um gráfico completo, tipos de paleta e daltonismo; desde 2026-11-10 com os tipos de atributo e a tarefa
  principal e as de apoio), com passos
  dentro do slide, notas do apresentador (tecla N), figuras redesenhadas em português, um gráfico do DATADOC por slide e
  exemplos brasileiros com os dados do material. `#todos` mostra todos os slides para imprimir em PDF.
- **Caderno** (`caderno.ipynb`): refaz cada gráfico com pandas e matplotlib a partir dos CSVs e confere os números com
  a página (asserts).

## Dados
| Dataset | Versão / consulta | Fonte original | Uso |
|---|---|---|---|
| ibge.municipios, ibge.censo2022_municipios, ibge.pib_municipios | 07/10/2026 | IBGE (API de localidades e SIDRA) | tabela de municípios (reaproveitada do Laboratório de hipóteses) |
| ibge.semiarido_2022, pi.territorios_desenvolvimento | 07/10/2026 | IBGE/Sudene; LC 87/2007 (compilação) | Aplicação 3 (construtor) |
| mds.bolsa_familia_municipios_serie | 13/10/2026 | MI Social / VIS DATA (MDS) | Aplicações 4, 5, 6, 8, 9, 10 |
| tse.resultados_2026_1t_presidente_municipios | 07/10/2026 | resultados.tse.jus.br | comparecimento por UF (Aplicações 1 e 5) |
| tse.eleitorado_local_votacao | 05/10/2026 | Portal de Dados Abertos do TSE | eleitores por UF (Aplicação 2) |
| inep.censo_escolar | 2025 (20/10/2026) | Microdados do INEP | matrículas por rede (Aplicação 7) |
| ibge.ipca_mensal | 09/10/2026 | SIDRA 1737 | IPCA do ano (Aplicação 2) |
| ibge.malha_ufs_2022 | 03/10/2026 | IBGE (geoftp) | mapa das UFs (Aplicações 5 e 10) |

## Método e decisões
- Dados reaproveitados dos materiais anteriores, com as regras deles: população do Censo 2022 como denominador;
  pessoas e famílias do mês de referência (set/2026); 4 municípios sem correspondência TSE ⇄ IBGE fora do
  comparecimento (L0001); 31 matrículas sem UF fora das barras.
- IPCA do ano = número-índice de dezembro ÷ dezembro do ano anterior − 1 (`variacao_anual_ipca`); 2009–2013
  reproduzem o gráfico de televisão dos slides (4,31 · 5,91 · 6,50 · 5,84 · 5,91).
- Histograma com faixas de largura fixa a partir de zero (`pandas.cut`, limite inferior incluído); Pearson em pandas
  sobre pares completos; malha das UFs simplificada (0,03°, 2 casas decimais, anéis no sentido horário para o d3) só
  para desenhar.
- Gráficos do professor (DATADOC / O POVO e OP+) embutidos na página nas tarefas perceptivas (decisão D2 de
  2026-11-10); imagens de terceiros (GraphCrimes, telejornal, mapa dos EUA, listras do aquecimento) só descritas em texto
  (D3). A simulação de deuteranopia (Machado, Oliveira e Fernandes, 2009) só transforma cores de apresentação.
- Nenhum gráfico responde a um problema de pesquisa: cada um ilustra uma tarefa perceptiva e diz o que não permite
  concluir. Nada é estimado ou preenchido.
- Lista de validação: `projetos/dataviz-didatico/docs/validacao-visualizacao.md`.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/preparar_laboratorio_hipoteses.py   # se faltar municipios.parquet
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/preparar_dados_abertos.py           # se faltarem os CSVs por UF
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/preparar_visualizacao.py
python -m labdados.produto_web projetos/dataviz-didatico/produtos/2026-11_visualizacao-de-dados
python projetos/dataviz-didatico/analise/caderno_visualizacao.py --rodar          # gera e confere o caderno
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/gerar_slides_visualizacao.py   # slides.html
pytest tests/test_dataviz_didatico_visualizacao.py
```

## Uso de IA
O desenho do material é do professor — os slides, o roteiro conceitual, a escolha das bases e as validações —, assim
como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos e ADRs),
amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq
nº 2.664/2026; a responsabilidade pelo conteúdo é do professor e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Leitura dos slides | Claude Code | exportar o deck e reorganizar os 50 slides em seis temas; descrever em texto os slides só de imagem | **pendente** (`docs/validacao-visualizacao.md`, seção 2) |
| Escolha e preparo dos dados | Claude Code | escolher, entre os dados já preparados pelo projeto, um conjunto por aplicação; IPCA anual, histograma, Pearson, malha das UFs | números conferidos por testes automáticos; escolhas **pendentes** de validação |
| Textos das aplicações | Claude Code | conceito, leituras guiadas, "o que o gráfico não diz", exemplos de código | **pendente** (selos `#revisao=1`) |
| Página e caderno | Claude Code | montagem da página (D3) e do caderno (pandas + matplotlib) | caderno executado com paridade; revisão visual pendente |
| Slides em HTML (2026-11-09) | Claude Code | a partir da revisão dos slides aceita pelo professor (“concordo com boa parte dos ajustes”): roteiro de 42 slides, figuras redesenhadas, gráficos com os dados do material, notas do apresentador com o texto dos slides originais | **pendente** (ajustes do professor) |
| Parte III · Atividade (2026-11-10) | Claude Code | a pedido do professor, com o briefing dele (três escolhas com o gráfico desenhado, comentário sem placar, uma hipótese por tarefa, recapitulação recolhida): escolha das cinco hipóteses e dos dados, comentários de cada opção, solução comentada, quadro das 20 hipóteses do Laboratório; desenhos, caderno e testes | **pendente** (`docs/validacao-visualizacao.md`, seção 8) |
| Atributos e tarefa principal (2026-11-10) | Claude Code | a partir das observações do professor (falta de referência para as tarefas perceptivas, com Munzner como ponto de partida; “quase todos têm múltiplas tarefas”; atributos antes das regras): conferência das referências, proposta (decisões do professor, D1–D7) e implementação — dois slides novos (atributos; tarefa principal e de apoio), textos dos exemplos e do exercício, figuras esquemáticas e demonstração na Aplicação 11 | **pendente** (`docs/validacao-visualizacao.md`, seção 9) |
| Atualização 0.4 (2026-11-10) | Claude Code | a pedido do professor, a partir dos slides que ele revisou e otimizou: comparação slide a slide e proposta (decisões do professor, D1–D6); implementação — Parte I em sete temas com o tema “Cor e acabamento”, figuras redesenhadas dos slides, gráficos do professor nas tarefas; Parte II reordenada, com as Aplicações 4 e 5 e o passo novo da tendência; caderno e testes | **pendente** (`docs/validacao-visualizacao.md`, seção 7) |
| Renovação 0.3 (2026-11-07) | Claude Code | a partir da segunda revisão do professor (sem testes nem jogo; demonstração cadenciada): Parte II em passos que redesenham só o quadro; galeria explicada no lugar do exercício | **pendente** |
| Renovação 0.2 (2026-11-07) | Claude Code | a partir da revisão do professor (marcas e canais mais bem explicados; tarefas uma a uma com exemplos; Parte II prática e dinâmica): figuras da Parte I, navegação das tarefas, jogo, construtor de gráfico, testes de leitura, “qual é a tarefa?” | **pendente** |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
