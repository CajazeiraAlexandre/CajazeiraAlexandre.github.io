# A evolução da rede federal de ensino

**Tipo:** visualização · **Projeto:** educacao · **Status:** rascunho (piloto)

## Pergunta
Como a rede federal de ensino (institutos e universidades) se espalhou pelo território entre 2000 e 2024, e em cada
governo: onde e quando surgiram as unidades, quantas matrículas e quanta população passou a ter uma unidade na sua região.

## Dados
| Dataset | Versão | Fonte original |
|---|---|---|
| `inep.censo_escolar` | padronizado 2001–2024 (critério do story `rede-federal-por-governo`) | INEP, microdados |
| `inep.censo_educacao_superior` | 2000–2008 (arquivos antigos e Sinopses), 2009–2024 (microdados) | INEP |
| `ibge.municipios_regiao_imediata`, `ibge.censo2022_municipios`, `ibge.malha_municipios_2022`, malha das UFs | cópias de 2026-10 | IBGE |
| `ibge.censo_escolaridade_25mais` | cópia de 2026-10-14 (SIDRA 3547 e 10061) | IBGE |
| `ibge.pnadc_anual_regioes` | cópia de 2026-10-12 (SIDRA 7269) | IBGE |
| `mec.novos_campi_if` | mapa de 07/08/2026, baixado pelo pesquisador | MEC |

## Método e decisões
- Decisões do pesquisador em 2026-10-14 (detalhes no `produto.yaml`): D1–D10 (proposta), Q1–Q8 (relatório de
  qualidade), A1–A3 (ampliação), V1–V5 (teste de papel). Resumo na folha ✎ Notas e fontes.
- ADRs: L0002 (cálculo no Python), L0003, L0007 (Visualização declarativa; componente do produto pela A16), L0017 (pilotos).
- Componente próprio: `src/extensao.js` (`rede_animada`), embutido pelo gerador (A16).

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/ibge/consultar_escolaridade_censos.py      # cópia local já versionada
PYTHONPATH=nucleo:. python fontes/mec/novos_campi_if.py
python projetos/educacao/analise/qualidade_evolucao_rede_federal.py
python projetos/educacao/analise/preparar_evolucao_rede_federal.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/educacao/produtos/2026-10_evolucao-rede-federal
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Proposta e qualidade | Claude (Claude Code, Anthropic) | propor método, levantar fontes e achados (máscara de 2000–2007, desmembramentos, intermitência) | decisões do pesquisador, 2026-10-14 |
| Dados | Claude (Claude Code) | escrever os pipelines (escolaridade, novos campi) e o preparo | relatório de qualidade validado; conferência dos números pendente |
| Página | Claude (Claude Code) | escrever o componente de animação e os textos | teste de papel aprovado; revisão final pendente |
| Ajustes de 2026-10-15 | Claude (Claude Code) | recortes do mapa, ▶ desde 2002, imagem fiel à tela, cores por governo (validadas com o script da skill dataviz), aviso de teste | revisão do pesquisador pendente |

## Pendências
- Validar os ajustes de 2026-10-15 (produto.yaml › ajustes_2026_10_15), em especial a paleta por governo e o recorte padrão (região imediata).
- Retratos dos presidentes (só com licença conferida, foto a foto; hoje as iniciais).
- Situação de cada novo campus (anunciado × autorizado a funcionar), pelas portarias do MEC.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
