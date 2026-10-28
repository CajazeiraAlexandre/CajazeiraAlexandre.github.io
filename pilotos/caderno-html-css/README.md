# HTML e CSS para layout: caderno de estudos e práticas

**Tipo:** material didático sem bases de dados (ADR PW0001) · **Projeto:** programacao-web-didatico · **Status:** rascunho (piloto 0.1, outubro de 2026) · **Página:** https://cajazeiraalexandre.github.io/pilotos/caderno-html-css/ (após publicação)

## Pergunta
Como revisar e praticar, com autonomia, o que foi dado em sala no 1º ano do curso Técnico em Informática (papéis de
HTML, CSS e JavaScript; estrutura do HTML; sintaxe CSS; tags semânticas; box model e fluxo; display e position;
Flexbox; Grid), de modo que quem já sabe pule ou revise um ponto específico e quem tem dificuldade siga passo a passo,
fechando com desafios de Flexbox e Grid.

## Estrutura
- **Apresentação:** objetivos de aprendizagem, duas trilhas ("já sei bastante" e "passo a passo"), autoria e uso de IA.
- **Parte I · Conceitos** (`src/conceitos.yaml`): oito seções, na ordem das aulas; cada uma com o quadro "Já sei?",
  texto, tabelas, editores embutidos, laboratórios de Flexbox e Grid (seletores que escrevem o CSS), mini-desafio,
  erros comuns e fontes (W3Schools, MDN).
- **Parte II · Práticas guiadas** (`src/praticas.yaml`): o site do Parque Nacional da Serra da Capivara em seis passos
  encadeados (esqueleto semântico → estilos → box model → display e position → Flexbox → Grid), com instruções,
  solução escondida e lista "Confira".
- **Parte III · Desafios** (`src/desafios.yaml`): quatro de Flexbox e quatro de Grid no formato da Quinta Lista de
  Exercícios da disciplina (enunciado em prosa, resultado esperado gerado pelo gabarito, HTML pronto, dicas
  progressivas, gabarito escondido). A entrega é combinada em sala.
- **Apoio** (`src/referencias.yaml`): trilhas, ferramentas, referências com links, slides, glossário de propriedades.

## Editor embutido
HTML (conteúdo do body) e CSS editáveis, resultado ao vivo num iframe sem scripts; Ctrl+Enter executa; Tab indenta.
O que o aluno digita fica só no navegador dele (localStorage, um registro por editor); "Restaurar" volta ao original;
"Copiar arquivo completo" monta o documento inteiro (doctype, head, body) para colar no VS Code. Funciona offline.

## Autoria, proposição e revisão
- **Autor e responsável:** Alexandre Ribeiro Cajazeira Ramos, professor da disciplina. São dele a concepção da
  disciplina, a sequência didática, os temas, as aulas, as listas e as práticas de onde o caderno deriva, e todas as
  decisões sobre conteúdo e avaliação.
- **Proposição (2026-10-28):** material de estudo e prática autônomo para o período sem aulas, com duas trilhas e
  desafios de Flexbox e Grid no formato das listas da disciplina. Decisões do professor: só o conteúdo dado em sala;
  sem questões objetivas; desafios novos com tema local; fontes W3Schools e MDN; entrega combinada em sala.
- **Revisão humana:** o estado de cada parte (revisado · testado · em revisão) está no bloco final da página e em
  `src/autoria.yaml › revisao.itens`, atualizado pelo professor a cada versão. Nesta versão, estrutura e decisões
  revisadas; código, soluções e gabaritos testados no navegador; textos da Parte I, enunciados e links em revisão.

## Sem dados, sem reconstrução (ADR PW0001)
Este material não usa bases de dados nem fontes oficiais: não há datasets, manifesto, relatório de qualidade,
caderno em pandas nem bloco de fontes e metodologia. O rodapé da página é o bloco "Autoria, revisão e uso de IA".
Vale o restante do laboratório: página autocontida (L0002) com os componentes do design system (L0003), objetivos de
aprendizagem declarados, referências com links, publicação só com aprovação do pesquisador.

## Como editar e remontar
```bash
python projetos/programacao-web-didatico/analise/preparar_caderno.py   # YAML de src/ → data/base.json.gz → index.html
```
Textos em `src/conceitos.yaml`, `praticas.yaml`, `desafios.yaml`, `referencias.yaml`; autoria, uso de IA e estado da
revisão em `src/autoria.yaml`. Edite o YAML, não o `index.html`.

## Uso de IA
O conteúdo, a sequência didática, os exemplos e os desafios são do professor, a partir dos slides, listas e práticas
da disciplina (briefing de 2026-10-28); os modelos e as especificações são do Laboratório de Dados Públicos. A tabela
registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do
pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Análise do material da disciplina | Claude (Anthropic, via Claude Code) | Ler slides, avaliações, formulários e trabalhos; identificar o que foi dado e o formato das listas | Pesquisador (chat de 2026-10-28) |
| Texto da Parte I | Claude | Reescrever os slides como texto de estudo, com tabelas, exemplos e erros comuns | Em revisão pelo professor (piloto 0.1) |
| Práticas e desafios | Claude | Escrever o site da Serra da Capivara em seis passos e os oito desafios com gabarito | Soluções e gabaritos testados no navegador; enunciados em revisão pelo professor |
| Editor e página | Claude | Editor embutido, laboratórios de Flex e Grid, montagem da página; bloco de autoria e ADR PW0001 redigidos a partir da orientação do professor | Testado no navegador (console sem erros); ADR aprovado pelo professor |

## Licença
Textos e exemplos: CC BY 4.0 · Código da página: MIT
