# O campus São Raimundo Nonato no Exame Classificatório do IFPI

Story (L0015), projeto `ifpi-srn`, para a gestão do campus SRN. Status: rascunho. Nos pilotos (L0017) desde
2026-11-13 (v0.3): https://cajazeiraalexandre.github.io/pilotos/srn-no-exame-classificatorio/

**Pergunta.** Como o campus SRN se posiciona no Exame Classificatório em relação ao IFPI? Quais os indicadores históricos
na região? Quais os cursos?

**Abrir:** `index.html` (duplo clique; celular, embed e modo apresentação 16:9 no mesmo arquivo).

## Como foi feito
1. Briefing (2026-11-13): região = região intermediária do IBGE; 2027.1 preliminar; pilotos; 8 a 10 cartões.
2. Cinco propostas de roteiro (`src/propostas-roteiro.md`, L0018); escolha do pesquisador: **a 1, com 3 e 4**.
3. Roteiro detalhado (`src/roteiro.yaml`) e prancha de leitura (`roteiro.html`); **validado** pelo pesquisador em 2026-11-13.
4. Montagem: `src/dados_story.py` lê só a base publicada do exploratório de origem
   (`2026-11_exame-classificatorio-2027-1`, `data/base.json.gz`) e preenche as frases e os cartões; o story é gerado pelo
   renderizador do laboratório (`viz.yaml`, lab-viz).

```bash
PYTHONPATH=nucleo:. .venv/bin/python projetos/ifpi-srn/produtos/2026-11_srn-no-exame-classificatorio/src/prancha.py
PYTHONPATH=nucleo:. .venv/bin/python projetos/ifpi-srn/produtos/2026-11_srn-no-exame-classificatorio/src/preparar_story.py
PYTHONPATH=nucleo:. .venv/bin/python -m labdados.viz og projetos/ifpi-srn/produtos/2026-11_srn-no-exame-classificatorio
```

5. **Roteiro v2 (validado pelo pesquisador em 2026-11-13; gerou a v0.2)**, a partir dos pedidos do pesquisador sobre a v0.1: régua de posições do
   exploratório no c1-3 ("senti falta do gráfico 1"); mesmo curso nos campi em barras, com seletores de curso e de turnos
   (no lugar do boxplot, "péssimo"); cursos do SRN com turnos somados como opção; séries com a opção "por ano"
   (1º + 2º semestre); "confirmadas por vaga" passa a "candidatos por vaga" (adendo da IS0003, também no exploratório);
   sai o cartão SRN × São João do Piauí. A v1 fica em `src/v1/`. Esboço no renderizador, antes de validar:
   `src/esboco.py` → `projetos/ifpi-srn/concepcao/2026-11-13_srn-story-v2-esboco/`.
6. **Ajustes da prancha v2 (pesquisador, 2026-11-13):** c2-2 com o contexto do IFPI (11 de 113 ofertas abaixo das vagas;
   Guia de Turismo só existe no SRN; Administração à tarde é a 26ª de 26; posição de cada curso na dica); c2-3 e c3-1
   com período 1º semestre | 2º semestre | por ano (no 2º semestre o SRN só abriu vagas em 2018.2, 2022.2 e 2024.2, sem
   Informática: a frase diz o que existe); "no SRN" vira "no IFPI-SRN" nas frases.
7. **Roteiro v3 (validado pelo pesquisador em 2026-11-13; gerou a v0.3)**, pedidos do pesquisador sobre a v0.2: sai o cartão 3 (oferta; a régua já mostra
   vagas e inscrições); cartões 5 e 6 abrem com manhã e tarde somadas; no cartão 7, anotação na lacuna de Informática de
   manhã em 2025.1 (ou 2025, por ano): "1ª turma do superior em TSI" (informação do pesquisador; nos relatórios, 2025.1
   tem Informática à tarde). A v2 fica em `src/v2/`; esboço em `projetos/ifpi-srn/concepcao/2026-11-13_srn-story-v3-esboco/`.
   2ª rodada (mesmo dia): o cartão do mesmo curso mostra todas as ofertas, com a forma na dica (a tarde de Administração do
   SRN, concomitante ou subsequente, não aparecia); cópia dele com Informática selecionada (c2-1b); série do Guia de
   Turismo no histórico dos cursos; "IFPI-SRN" onde o texto fala do campus e "São Raimundo Nonato" onde fala da cidade.

## Dados
Os mesmos do exploratório (IS0001–IS0003): Demonstrativo de inscrições de 13/11/2026 (preliminar), Edital 56/2026 e
retificações, relatórios de Concorrência de 2018.2 a 2026.2 (`ifpi.exame_classificatorio`); regiões e população de 14 a
17 anos do IBGE.

## Decisões locais (ajustes na montagem, confirmados pelo pesquisador em 2026-11-13)
- c1-2: barras de vagas por campus, com as inscrições entre parênteses, no lugar da dispersão vagas × inscritos (o
  adaptador de dispersão do story só desenha dentro de uma Visualização; barras de inscrições ficavam esmagadas pelas
  7.369 de Teresina Central). Frase do cartão igual; nota refeita.
- c2-3: só edições completas (2019.1 a 2026.1), como diz o subtítulo; o ponto de 2027.1 (preliminar) fica no c3-1.
- Capa: subtítulo encurtado ("Procura, cursos e região, 2018–2027"), que cortava no celular.
- Renderizador de stories (lab-viz): `linhas` ganhou `opcoes.formato` (valores que não são %) e o `boxplot`, pontos em
  destaque (`destaque`, `rotulo_curto`) — extensões compatíveis com os stories existentes.
- v2: o lab-viz ganhou o adaptador `regua_posicoes` (experimental no story; o desenho de `Lab.reguaPosicoes` da página,
  com tocar para seguir um campus e a sua região). Nos cartões com seletor, o subtítulo é só o seletor ("Ver: …") e o
  texto vai para a nota: no celular o subtítulo tem uma linha e cortava os botões.
- Ajustes da prancha v2, nos componentes comuns: no `lab-viz.css`, o subtítulo que contém seletor deixa de ser cortado
  em uma linha no celular (exceção à Q-098; com três períodos e dois turnos, o c2-3 escondia os botões de turno); no
  `linhas`, uma série com até 4 pontos ganha o valor ao lado de cada ponto solto (o SRN no 2º semestre). As duas mudanças
  só aparecem quando o caso ocorre (seletor longo, série esparsa), também em outros stories.
- v3: o `linhas` passa a aceitar anotações ancoradas (Q-096): `posicao("série:momento")` é o ponto e
  `posicao("lacuna:série:momento")`, o vão de uma série sem valor naquele momento, só quando o vão existe. Com outra opção
  do seletor, a anotação some sozinha.

## Uso de IA (Portaria CNPq nº 2.664/2026)
A pergunta, o briefing, a escolha da proposta de roteiro e a validação do roteiro são do pesquisador, assim como as
decisões de método do projeto (IS0001–IS0003) e os pedidos que formaram o exploratório de origem. O processo de story
(propostas, roteiro, prancha), os modelos e o renderizador são do laboratório, amadurecidos pelo pesquisador com apoio
dos agentes. Dentro desse quadro, o Claude Code (Anthropic, Claude Opus 5.5) redigiu as cinco propostas e o roteiro,
escreveu o preparo dos números e dos cartões, fez as extensões do renderizador e montou o story. **Verificação humana da
versão montada: pendente.** A responsabilidade pelo conteúdo é do pesquisador; a IA não é autora.
