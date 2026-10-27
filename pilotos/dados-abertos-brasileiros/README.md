# Antes de analisar: definir, obter e checar com dados abertos brasileiros

**Tipo:** didatico · **Projeto:** dataviz-didatico · **Status:** rascunho (piloto 0.2 em validação) · **Página (pilotos):** https://cajazeiraalexandre.github.io/pilotos/dados-abertos-brasileiros/

## Pergunta
Onde estão os dados abertos brasileiros úteis para diferentes frentes, que problemas cada base permite formular e como
passar por ela nas três etapas iniciais do fluxo de dados — definição do problema, obtenção e checagem — e no que vem
antes de analisar. Público: graduação em Tecnologia em Sistemas para Internet (IFPI), disciplina de visualização de
dados. O material precede o Laboratório de hipóteses: para na porta da análise.

## Estrutura
- **Parte I · Conceitos** (`src/parte1.yaml`): fluxo de trabalho, definição, natureza das fontes, obtenção e checagem —
  a partir da Aula 1; complementos marcados com `c: true`.
- **Parte II · Expedições** (`src/app.js`): TSE, IBGE, Portal da Transparência e Tesouro, MDS e INEP, cada uma em
  quatro etapas (revisão de 2026-10-27): **definição** (um problema que pede análise, com duas ou três hipóteses de
  trabalho, unidade, recorte, variáveis e natureza do dado) → **obtenção** (onde procurar, candidatas encontradas e
  decisão; depois download ou API) → **checagem** (só consistência, integridade e semântica, com os problemas reais da
  base; gráfico só quando serve à checagem) → **antes de analisar: caminhos** (hipótese → operações → estatística
  descritiva → o que corroboraria; sem números) — com leitura guiada e código em pandas; e o mapa das fontes
  (`src/fontes.yaml`).
- **Parte III · Desafios**: dois desafios (formular ou ampliar um problema; seguir para a análise a partir de uma
  expedição), campos da ficha, lista de checagem e exemplo; formato de entrega livre, sem formulário nem exportação;
  datas e especificações da entrega pactuadas pelo professor em sala. O desafio B tem gabarito e modelo na Parte III · Desafios do *Laboratório de hipóteses*, que examina as quinze
  hipóteses das expedições (decisão do pesquisador, 2026-10-27).
- **Apoio** (`src/referencias.yaml`): objetivos, autoria, uso de IA, referências, bases e CSVs.
- **Caderno** (`caderno.ipynb`): refaz a obtenção e a checagem a partir das fontes e confere os números com as tabelas
  da página; a etapa "antes de analisar" aparece como código não executado.

## Dados
| Dataset | Versão / consulta | Fonte original |
|---|---|---|
| tse.eleitorado_local_votacao | 2026 (baixado em 05/10/2026) | Portal de Dados Abertos do TSE |
| tse.resultados_2026_1t_presidente_municipios | 07/10/2026 | resultados.tse.jus.br (JWS assinados) |
| ibge.municipios, ibge.censo2022_municipios, ibge.pib_municipios | 07/10/2026 | IBGE (API de localidades e SIDRA) |
| ibge.populacao_estimada_uf | 19/10/2026 | SIDRA 6579, 1378, 4709 |
| ibge.ipca_mensal | 09/10/2026 (até set/2026) | SIDRA 1737 |
| transparencia.despesa_funcional_educacao | 14/10/2026 | API do Portal da Transparência (CGU) |
| tesouro.despesas_mensais_uniao | só o manifesto (arquivo gerado em 19/06/2019) | Tesouro Transparente |
| mds.bolsa_familia_municipios_serie | 13/10/2026 | MI Social / VIS DATA (MDS) |
| inep.censo_escolar | 2024 e 2025 (2025 baixado em 20/10/2026) | Microdados do INEP |
| inep.censo_educacao_superior | 2024 | Microdados do INEP |

## Método e decisões
Decisões do pesquisador em 2026-10-20 (`produto.yaml › metodo`):
- peças por UF, com o Piauí em destaque quando houver dado por município; ano mais recente de cada base;
- correção monetária pelo IPCA até o mês mais recente (set/2026), com a **média do índice no ano** como base de cada
  ano (D4): desde 2026-10-27 só como operação descrita na etapa 4, com o fator no CSV (a página mostra nominais);
  2026 da Transparência à parte (ano parcial);
- ensino superior: só graduação (os 393 sequenciais em nota);
- anomalias (pago > liquidado; salto da educação profissional estadual no PI em 2025) mostradas como "a investigar";
- checagem do IBGE pela quebra de série estimativa × Censo (no lugar dos símbolos do SIDRA);
- Censo Escolar 2025 padronizado no pipeline comum (`fontes/inep/padronizar.py --escolar-2025`, D8);
- dados.gov.br retirado por ora (API exige chave pessoal).

Revisão de 2026-10-27 (`produto.yaml › revisao_2026_10_27`): as expedições produziam gráficos e respostas quando o
material deve parar antes da análise. Gráficos-resposta retirados (eleitores por UF, despesa corrigida, matrículas por
rede, graduação EAD); ficam os gráficos de checagem (dupla contagem do ZIP do TSE, quebra estimativa × Censo, fases da
despesa com o ano parcial, lacunas do MDS, linhas × cursos distintos do INEP). Hipóteses verificáveis com estatística
descritiva — localização, variabilidade, distribuição, boxplot; correlação (Pearson) só quando a hipótese é de relação.
Em 27/10/2026 a API do MI Social (MDS) redirecionava para a página de avisos do ministério; o caderno informa e usa a
cópia do material.
Relatório de qualidade: `projetos/dataviz-didatico/docs/relatorio-qualidade-dados-abertos.md`.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/inep/baixar.py --anos 2025 2025 --so escolar      # se faltar o Censo Escolar 2025
PYTHONPATH=nucleo:. python fontes/inep/padronizar.py --escolar-2025
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/relatorio_qualidade_dados_abertos.py
PYTHONPATH=nucleo:. python projetos/dataviz-didatico/analise/preparar_dados_abertos.py
python -m labdados.produto_web projetos/dataviz-didatico/produtos/2026-10_dados-abertos-brasileiros
python projetos/dataviz-didatico/analise/caderno_dados_abertos.py --rodar          # gera e confere o caderno
pytest tests/test_dataviz_didatico_dados_abertos.py
```

## Uso de IA
O desenho do material é do professor — pergunta, briefing, escolha das fontes, recortes, decisões de método (como a
correção pelo IPCA) e validações —, assim como os modelos e as especificações do laboratório em que o assistente
trabalha (CLAUDE.md, modelos e ADRs), amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou
dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do professor e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de estrutura e de dados | Claude (Anthropic), Claude Code | organizar as opções a partir do briefing | escolhas do professor em 2026-10-20 (estrutura C, fontes, D1–D8) |
| Relatório de qualidade | Claude Code | medir os problemas reais de cada base e conferir totais oficiais | relatório validado pelo professor (D1–D8) |
| Pipelines e preparo | Claude Code | download do Censo Escolar 2025, padronização, base da página, testes do IPCA | números conferidos por script e com totais oficiais |
| Textos | Claude Code | complementos da Parte I, cartões de checagem, leituras guiadas, mapa das fontes | **pendente** — trechos com `c: true` (`docs/validacao-dados-abertos.md`) |
| Página e caderno | Claude Code | montagem da página e do caderno (pandas) | caderno executado com paridade; revisão visual pendente |
| Revisão 0.2 (2026-10-27) | Claude Code | a partir das orientações do professor (etapas, checagem, busca, caminhos, desafios): rascunho dos problemas e hipóteses, dos blocos de busca, das etapas "antes de analisar" e da Parte III; gráficos de checagem novos | decisões 1a–5a do professor; textos **pendentes** de validação (selos `#revisao=1`) |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
