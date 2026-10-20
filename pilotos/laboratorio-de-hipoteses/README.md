# Laboratório de hipóteses: estatística descritiva e análise exploratória de dados

**Tipo:** material didático · **Versão:** 1.0 (piloto, outubro de 2026) · **Página:** https://cajazeiraalexandre.github.io/pilotos/laboratorio-de-hipoteses/

## Pergunta
Como média, mediana, desvio padrão, coeficiente de variação, quartis e intervalo interquartil (e a correlação)
descrevem dados públicos reais, e como usá-los, com filtrar, agrupar e ordenar, para formular e examinar uma hipótese,
sem inferência estatística. Público: graduação (disciplina de visualização de dados).

## Estrutura
- **Parte I · Conceitos** (`src/parte1.yaml`): estatística descritiva e AED a partir dos slides do professor; complementos marcados com `c: true`.
- **Parte II · Aplicação** (`src/app.js`): aplicações 0–7 com os municípios brasileiros, leituras guiadas e exemplos de código em pandas; a Aplicação 6 examina cinco hipóteses com critério de leitura declarado.
- **Parte III · Desafios**: em preparação.
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

## Como reproduzir
```bash
python fontes/mds/consultar_bolsa_familia_serie.py --confirmar-ate-mb 35   # só para atualizar a série
python projetos/dataviz-didatico/analise/preparar_laboratorio_hipoteses.py
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

## Licença
Código: MIT · Dados derivados: CC BY 4.0
