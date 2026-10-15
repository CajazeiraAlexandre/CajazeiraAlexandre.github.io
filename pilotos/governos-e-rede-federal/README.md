# O que cada governo fez pela rede federal de ensino

**Tipo:** story · **Projeto:** educacao · **Status:** rascunho (primeira versão para avaliação, 2026-10-14)

## Pergunta
Pergunta central do pesquisador: quem valoriza e interioriza a rede federal de ensino? O story descreve, governo a
governo (2003–2024), onde a rede chegou, quanto cresceu no interior, o quadro de docentes e a assistência estudantil —
e termina no mapa ("procure a sua cidade").

## Roteiro
Proposta 1 (a rede que foi para o interior) + segundo ato da proposta 4 (as pessoas) — `src/propostas-roteiro.md`
(L0018). Roteiro detalhado ainda não escrito: esta versão serve para avaliar o arco.

## Dados
| Dataset | Uso |
|---|---|
| base da Visualização `2026-10_evolucao-rede-federal` (INEP, IBGE, MEC) | regiões, unidades, interior, ampliação, implantação, mapa |
| `inep.censo_educacao_superior` | docentes em exercício (Sinopses 2001–2008, microdados 2009–2024) |
| `tesouro.despesas_mensais_uniao` | assistência estudantil 2008–2013 (`analise/tesouro_acoes_educacao.py`) |
| `transparencia.despesa_funcional_educacao` | assistência estudantil 2014–2025 |
| `ibge.ipca_mensal`, `ibge.inpc_mensal` | correção monetária: IPCA no gasto, INPC no salário (L0019) |
| `mgi.tabela_remuneracao` | salário docente: Tabela de Remuneração (2002–2012) e anexos da Lei 12.772 (2013–2024) — `fontes/mgi/baixar_tabela_remuneracao.py` |

## Como reproduzir
```bash
python projetos/educacao/analise/preparar_evolucao_rede_federal.py
python projetos/educacao/analise/tesouro_acoes_educacao.py
PYTHONPATH=nucleo:. python fontes/mgi/baixar_tabela_remuneracao.py
python projetos/educacao/produtos/2026-10_governos-e-rede-federal/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/educacao/produtos/2026-10_governos-e-rede-federal
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude (Claude Code, Anthropic) | cinco propostas (L0018) | escolha do pesquisador (1 e 4), 2026-10-14 |
| Dados e textos | Claude (Claude Code) | preparo dos cartões e textos da primeira versão | pendente |
| Ajustes de 2026-10-15 | Claude (Claude Code) | salário no topo da carreira, governos em faixas coloridas nas séries, início em 2002, cores por governo, aviso de teste | revisão do pesquisador pendente |

## Pendências
- Validar os ajustes de 2026-10-15 (produto.yaml › ajustes_2026_10_15), em especial a paleta por governo e o recorte padrão (região imediata).
- Roteiro detalhado e prancha (L0018, portão 2).
- Validar as escolhas provisórias do salário: GED na pontuação máxima até 2005; mês de referência (posição da edição até 2012; dezembro desde 2013); 2009 pela edição nº 48.
- Docentes da rede profissional antes de 2013.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
