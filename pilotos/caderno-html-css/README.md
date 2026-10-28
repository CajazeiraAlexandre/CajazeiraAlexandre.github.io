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

## Decisão local: versão adaptada para baixa visão
Pedido do professor (2026-10-28): a turma tem alunos com necessidades específicas, em especial baixa visão, e o
material precisa de uma opção que amplie a acessibilidade. A opção **"Baixa visão"**, no alto da página, liga uma
versão adaptada e guarda a escolha no navegador e no endereço (`#acesso=baixa-visao&escala=150&tema=escuro`), de modo
que o professor pode mandar o link já adaptado. O que muda, e a diretriz correspondente (WCAG 2.2; nota do W3C/WAI
*Accessibility Requirements for People with Low Vision*, 2016):

- **Texto maior**, de 125% a 200% (padrão 150%), com entrelinha 1,7, espaçamento entre letras e palavras e parágrafos
  mais separados (1.4.4 Redimensionar texto; 1.4.8 Apresentação visual; 1.4.12 Espaçamento de texto). Todos os tamanhos
  do caderno estão em `rem`, por isso escalam juntos e também respeitam o tamanho padrão configurado no navegador.
- **Contraste alto**, nível AAA: texto preto sobre branco, texto secundário sem cinza claro, bordas e divisórias mais
  escuras, links sempre sublinhados, chips sem fundo colorido (1.4.6 Contraste reforçado; 1.4.1 Uso da cor).
- **Fundo escuro** opcional (texto branco sobre preto), para quem tem fotofobia ou lê melhor em claro-sobre-escuro;
  usa a paleta escura do design system do laboratório com as mesmas correções de contraste.
- **Uma coluna**: código e resultado dos editores empilhados, abas estáticas, laboratórios em coluna, para não perder
  largura quando o texto cresce (1.4.10 Refluxo).
- **Foco visível** (contorno de 3 px) e **alvos maiores** (botões e seletores com pelo menos 44 px) (2.4.7; 2.5.8).
- **Resultado ampliado**: a pré-visualização dos editores e o "Resultado esperado" dos desafios recebem o mesmo fator
  de ampliação (zoom na raiz do iframe, como o zoom do navegador), para que o aluno veja o que construiu. O arquivo
  aberto em nova aba ou copiado sai sempre no tamanho real.

Fora do escopo desta versão: leitor de tela dedicado (a página já usa marcação semântica, `aria-label` e tabelas
reais), teclado alternativo nos editores e legendas de áudio. A validação com os próprios alunos está pendente
(quadro de revisão). Se um segundo material precisar da mesma opção, ela é candidata a entrar nos componentes do
laboratório (promoção registrada em ADR, CLAUDE.md § 3).

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
| Versão para baixa visão (0.2) | Claude | Implementar a opção pedida pelo professor a partir das diretrizes WCAG 2.2 e da nota do W3C/WAI sobre baixa visão | Testado no navegador em 150% e 200%, claro e escuro; validação com os alunos pendente |

## Licença
Textos e exemplos: CC BY 4.0 · Código da página: MIT
