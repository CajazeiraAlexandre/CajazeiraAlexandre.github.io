# Contando histórias a partir de dados: visualização de dados

**Tipo:** didatico · **Projeto:** dataviz-didatico · **Status:** rascunho (piloto 0.3 em validação) · **Página (IFPI 2026.2):** https://cajazeiraalexandre.github.io/ifpi-2026-2/visualizacao-de-dados/

## Pergunta
Por que visualizar dados, como um gráfico é construído (marcas, canais e atributos) e como escolhê-lo pela tarefa
perceptiva do leitor — comparar, parte/todo, tendência temporal, distribuição e correlação, observação ampla —, com
as ferramentas disponíveis. Terceiro material da série da disciplina (Tópicos Especiais; graduação em Tecnologia em
Sistemas para Internet, IFPI), a partir dos slides "Contando histórias a partir de dados — Visualização". Sem Parte
III (desafios) nesta primeira versão (pesquisador, 2026-11-07).

## Estrutura
- **Parte I · Conceitos** (`src/parte1.yaml`), em seis temas: o que é visualizar (um gráfico é uma tradução: dados →
  codificação visual → percepção); por que visualizar (velocidade da visão, atributos pré-atentivos com um teste
  interativo, quarteto de Anscombe); visualizar também pode confundir (esquemas das quatro armadilhas); **marcas e
  canais** explicados com figuras (as três marcas; os canais desenhados; a ordem de eficácia de Munzner; as regras de
  expressividade e eficácia; a receita de quatro passos para descrever ou montar um gráfico; os esquemas A–D dos
  slides com a resposta); **tarefas perceptivas, uma a uma** (navegação 1–5: definição dos slides, o que o leitor
  pergunta, marcas e canais, gráficos, cuidados, exemplo dos slides, link para a aplicação); ferramentas. Texto dos
  slides da disciplina; complementos do assistente marcados com `c: true`.
- **Parte II · Aplicações** (`src/app.js`), demonstrações cadenciadas na ordem da Parte I, com dados públicos
  reais — cada aplicação é uma sequência de passos que troca o gráfico no lugar (sem recarregar a página), com um
  texto por passo: 1 **Da tabela ao gráfico** (tabela → barras → ordenadas → valor e cor); 2 **Os esquemas A–D com
  dados reais** (B → C → D → errado de propósito → A), mais um construtor recolhido para montar o próprio gráfico
  com verificação de expressividade e eficácia; 3 **As armadilhas** (IPCA da TV → eixo em zero → contexto 1995–2025;
  pizza de 27 fatias → barras); 4–8 **uma aplicação por tarefa perceptiva**, cada uma com o quadro “o leitor pergunta
  → a tarefa → a escolha”, os passos que constroem o gráfico, uma leitura guiada curta, “o que o gráfico não diz” e o
  código em pandas; 9 **A tarefa de cada gráfico** (a galeria dos slides 43–47, com a resposta explicada); 10 **Agora
  você** (a atividade do slide 50). Sem testes nem jogo (revisão do professor, 2026-11-07).
- **Apoio** (`src/referencias.yaml`): objetivos, autoria, uso de IA, slides, referências, bases (onde e como baixar),
  CSVs, materiais anteriores, como citar.
- **Slides** (`slides.html`, 2026-11-09): versão HTML revista dos slides da aula, conforme a revisão em
  `projetos/dataviz-didatico/docs/2026-11-09_revisao-slides-visualizacao.md` — 42 slides em cinco partes, com passos
  dentro do slide, notas do apresentador (tecla N), figuras redesenhadas em português, um gráfico do DATADOC por slide e
  exemplos brasileiros com os dados do material. `#todos` mostra todos os slides para imprimir em PDF.
- **Caderno** (`caderno.ipynb`): refaz cada gráfico com pandas e matplotlib a partir dos CSVs e confere os números com
  a página (asserts).

## Dados
| Dataset | Versão / consulta | Fonte original | Uso |
|---|---|---|---|
| ibge.municipios, ibge.censo2022_municipios, ibge.pib_municipios | 07/10/2026 | IBGE (API de localidades e SIDRA) | tabela de municípios (reaproveitada do Laboratório de hipóteses) |
| ibge.semiarido_2022, pi.territorios_desenvolvimento | 07/10/2026 | IBGE/Sudene; LC 87/2007 (compilação) | Aplicação 3 |
| mds.bolsa_familia_municipios_serie | 13/10/2026 | MI Social / VIS DATA (MDS) | Aplicações 4, 6, 7, 8 |
| tse.resultados_2026_1t_presidente_municipios | 07/10/2026 | resultados.tse.jus.br | comparecimento por UF (Aplicação 1) |
| tse.eleitorado_local_votacao | 05/10/2026 | Portal de Dados Abertos do TSE | eleitores por UF |
| inep.censo_escolar | 2025 (20/10/2026) | Microdados do INEP | matrículas por rede (Aplicação 5) |
| ibge.ipca_mensal | 09/10/2026 | SIDRA 1737 | IPCA do ano (Aplicação 2) |
| ibge.malha_ufs_2022 | 03/10/2026 | IBGE (geoftp) | mapa das UFs (Aplicação 8) |

## Método e decisões
- Dados reaproveitados dos materiais anteriores, com as regras deles: população do Censo 2022 como denominador;
  pessoas e famílias do mês de referência (set/2026); 4 municípios sem correspondência TSE ⇄ IBGE fora do
  comparecimento (L0001); 31 matrículas sem UF fora das barras.
- IPCA do ano = número-índice de dezembro ÷ dezembro do ano anterior − 1 (`variacao_anual_ipca`); 2009–2013
  reproduzem o gráfico de televisão dos slides (4,31 · 5,91 · 6,50 · 5,84 · 5,91).
- Histograma com faixas de largura fixa a partir de zero (`pandas.cut`, limite inferior incluído); Pearson em pandas
  sobre pares completos; malha das UFs simplificada (0,03°, 2 casas decimais, anéis no sentido horário para o d3) só
  para desenhar.
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
| Renovação 0.3 (2026-11-07) | Claude Code | a partir da segunda revisão do professor (sem testes nem jogo; demonstração cadenciada): Parte II em passos que redesenham só o quadro; galeria explicada no lugar do exercício | **pendente** |
| Renovação 0.2 (2026-11-07) | Claude Code | a partir da revisão do professor (marcas e canais mais bem explicados; tarefas uma a uma com exemplos; Parte II prática e dinâmica): figuras da Parte I, navegação das tarefas, jogo, construtor de gráfico, testes de leitura, “qual é a tarefa?” | **pendente** |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
