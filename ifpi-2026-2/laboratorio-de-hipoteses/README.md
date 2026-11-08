# Laboratório de hipóteses: estatística descritiva e análise exploratória de dados

**Tipo:** material didático · **Versão:** 1.1 (piloto, outubro de 2026; Parte III em 2026-10-27) · **Página:** https://cajazeiraalexandre.github.io/ifpi-2026-2/laboratorio-de-hipoteses/

## Pergunta
Como média, mediana, desvio padrão, coeficiente de variação, quartis e intervalo interquartil (e a correlação)
descrevem dados públicos reais, e como usá-los, com filtrar, agrupar e ordenar, para formular e examinar uma hipótese,
sem inferência estatística. Público: graduação (disciplina de visualização de dados).

## Estrutura
- **Parte I · Conceitos** (`src/parte1.yaml`): estatística descritiva e AED a partir dos slides do professor; complementos marcados com `c: true`.
- **Parte II · Aplicação** (`src/app.js`): aplicações 0–7 com os municípios brasileiros, leituras guiadas e exemplos de código em pandas; a Aplicação 6 examina cinco hipóteses com critério de leitura declarado.
- **Parte III · Desafios** (`src/app.js › DESAFIOS`, 2026-10-27): a continuação das cinco expedições do material
  *Antes de analisar* — as quinze hipóteses de trabalho (três por expedição) examinadas com o roteiro da Aplicação 6
  (hipótese, operacionalização, previsão, critério declarado antes, operações, resultado, "contra a hipótese",
  limites, leitura guiada, código em pandas) e, ao fim, o bloco "Agora você: novos horizontes" (2026-11-03): o
  trabalho prático pede hipóteses próprias — outra pergunta sobre os mesmos dados, cruzamento de bases do material ou
  outra fonte —, com os CSVs e o modelo de ficha; refazer um desafio é possível, mas menos recomendado.
  Dados da Parte III em `analise/preparar_desafios.py` (seções do Piauí, despesa por ação, matrículas do INEP).
- **Referências e dados** (`src/referencias.yaml`): apresentação (autoria, IA), slides, referências com links, bases (onde e como baixar) e os CSVs do material.

## Dados
| Dataset | Versão | Fonte original |
|---|---|---|
| `ibge.municipios` | cópia de 2026-10-07 | IBGE, API de localidades |
| `ibge.censo2022_municipios` | cópia de 2026-10-07 | IBGE, SIDRA 10211, 9543, 10295 |
| `ibge.pib_municipios` | cópia de 2026-10-07 (PIB 2022) | IBGE, SIDRA 5938 |
| `mds.bolsa_familia_municipios_serie` | cópia de 2026-10-13 (jan/2006–set/2026) | MDS, MI Social / VIS DATA |
| `tse.resultados_2026_1t_presidente_municipios` | coleta de 2026-10-07 | TSE, resultados oficiais |
| `ibge.semiarido_2022` | lista 2022 | IBGE / Sudene |
| `pi.territorios_desenvolvimento` | tabela de referência | LC 87/2007; Lei 6.967/2017 |
| `tse.eleitorado_local_votacao` (Parte III) | 2026, baixado em 2026-10-05 | TSE, Portal de Dados Abertos (arquivo PI) |
| `transparencia.despesa_funcional_educacao` + `ibge.ipca_mensal` (Parte III) | consulta de 2026-10-14; IPCA até set/2026 | Portal da Transparência (API); SIDRA 1737 |
| `inep.censo_escolar` (Parte III) | 2025, baixado em 2026-10-20 | INEP, microdados |
| `inep.censo_educacao_superior` (Parte III) | 2024 | INEP, microdados |

## Método e decisões
- Decisão metodológica citada: L0001 (correspondência de municípios TSE ⇄ IBGE). A página é autocontida (abre sem
  servidor) e só faz cálculos leves no navegador, conferidos por teste de paridade com as funções Python.
- Decisões locais (pesquisador, 2026-10-13; detalhes no `produto.yaml`):
  - métricas pelo padrão do pandas: quartis por interpolação linear, desvio padrão amostral; outliers por 1,5 × IQR e
    |z| > 3, só sinalizados;
  - Bolsa Família: 2006–2026, um mês por ano (dezembro; setembro em 2026), Auxílio Brasil no período nov/2021–fev/2023,
    cancelamentos a partir de 2014 (acumulado e média mensal), denominador = população do Censo 2022;
  - Itaubal (AP) fora do indicador de cobertura de 2026; 4 municípios sem par TSE ⇄ IBGE fora do comparecimento;
    Boa Esperança do Norte (MT) ausente nas variáveis de 2022.
- Relatório de qualidade: `projetos/dataviz-didatico/docs/relatorio-qualidade-laboratorio-hipoteses.md`.
- **Parte III (2026-10-27, pesquisador):** critérios de leitura novos, declarados na página e na metodologia
  (concentração: 10% maiores ≥ 50%; assimetria: Bowley ≥ 0,2 com média acima da mediana; dentro × entre UFs: razão
  de IQRs ≥ 1,5; série real: ≥ 3 quedas; amplitude pago ÷ empenhado ≥ 10 pontos; saltos: cinco maiores > 50% da
  variação absoluta; redes: IQR da federal < metade do menor dos outros) — convenções validadas pelo pesquisador em 2026-11-03. Funções
  de referência `bowley` e `concentracao` em `metricas.py`, espelhadas no JS com paridade. Resultados em 2026-10-27:
  TSE — H1 corroborada (10% maiores municípios = 51,0% do eleitorado), H2 contrariada (Bowley −0,27: as seções têm
  teto), H3 inconclusiva; IBGE — H1 contrariada (razão 0,54), H2 corroborada (Bowley 0,23; 305 atípicos), H3
  inconclusiva (Pearson 0,06); Transparência — H1 corroborada (4 quedas reais; nominal +99% × real +8%), H2
  corroborada (10% maiores ações = 91,6%), H3 inconclusiva (amplitude 8,6 pontos); MDS — H1 corroborada, H2
  contrariada (cinco maiores saltos = 24%), H3 contrariada (Pearson −0,55); INEP — H1, H2 e H3 corroboradas.
- Em 27/10/2026 a API do MI Social (MDS) redirecionava para a página de avisos do ministério; a Parte III usa a cópia
  local datada do laboratório.

## Como reproduzir
```bash
python fontes/mds/consultar_bolsa_familia_serie.py --confirmar-ate-mb 35   # só para atualizar a série
python projetos/dataviz-didatico/analise/preparar_laboratorio_hipoteses.py   # inclui preparar_desafios.py (Parte III)
python -m labdados.produto_web projetos/dataviz-didatico/produtos/2026-10_laboratorio-de-hipoteses
pytest tests/test_dataviz_didatico_metricas.py tests/test_dataviz_didatico_paridade.py
```

## Uso de IA
O desenho do produto é do pesquisador — pergunta, briefing, recortes, decisões de método e validações —, assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos e ADRs), amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Proposta e briefing | Claude (Claude Code, Anthropic) | redigir a proposta, levantar as bases e os campos da API do MDS | decisões do pesquisador em 2026-10-13 (proposta v1–v3) |
| Dados | Claude (Claude Code) | escrever o pipeline da série do Bolsa Família e o script de preparação | relatório de qualidade validado pelo pesquisador (2026-10-13) |
| Métricas | Claude (Claude Code) | escrever as funções de referência, o espelho JS e os testes | testes de unidade e de paridade; conferência pelo pesquisador pendente |
| Página | Claude (Claude Code) | escrever as aplicações, a Parte I a partir dos slides, as leituras guiadas e as hipóteses H3–H5 | piloto em aula; pendências no arquivo de validação |
| Parte III · Desafios (2026-10-27) | Claude (Claude Code) | a partir da decisão do professor (desafios = continuação das expedições): preparar os dados, propor os critérios de leitura novos, escrever os quinze desafios, as funções de referência e os testes de paridade | critérios, operacionalizações, textos e bases validados pelo pesquisador em 2026-11-03 (`docs/validacao-laboratorio-hipoteses.md`); números conferidos por teste de paridade |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
