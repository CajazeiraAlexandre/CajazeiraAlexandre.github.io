# O que cada governo fez pela rede federal de ensino

**Tipo:** story · **Projeto:** educacao · **Status:** rascunho · **Versão:** 0.1 (2026-10-15), fechada para o ambiente de pilotos

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
| `ibge.ipca_mensal` | correção monetária: IPCA no gasto (L0019) |

## Como reproduzir
```bash
python projetos/educacao/analise/preparar_evolucao_rede_federal.py
python projetos/educacao/analise/tesouro_acoes_educacao.py
python projetos/educacao/produtos/2026-10_governos-e-rede-federal/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/educacao/produtos/2026-10_governos-e-rede-federal
```

## Uso de IA
O desenho do produto é do pesquisador — pergunta, briefing, recortes, decisões de método e validações —, assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos e ADRs), amadurecidos por ele com apoio dos agentes. A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude (Claude Code, Anthropic) | cinco propostas (L0018) | escolha do pesquisador (1 e 4), 2026-10-14 |
| Dados e textos | Claude (Claude Code) | preparo dos cartões e textos da primeira versão | pendente |
| Ajustes de 2026-10-15 | Claude (Claude Code) | salário no topo da carreira, governos em faixas coloridas nas séries, início em 2002, cores por governo, aviso de teste | revisão do pesquisador pendente |
| Ampliação e áreas (2026-10-15) | Claude (Claude Code) | proposta (src/proposta-ampliacao-e-areas.md), medidas por governo, mapa de ampliação, áreas CINE, cartões de Picos | decisões do pesquisador Q1–Q6; conferência dos números pendente |

## Pendências
- Validar as escolhas de implementação da ampliação (quebra de fonte dos cursos em 2009; classes por quartis absolutos) — src/proposta-ampliacao-e-areas.md da Visualização.
- Salário docente retirado do story em 2026-10-15 (pedido do pesquisador).
- Validar os ajustes de 2026-10-15 (produto.yaml › ajustes_2026_10_15), em especial a paleta por governo e o recorte padrão (região imediata).
- Roteiro detalhado e prancha (L0018, portão 2).
- Docentes da rede profissional antes de 2013.

## Licença
Código: MIT · Dados derivados: CC BY 4.0
