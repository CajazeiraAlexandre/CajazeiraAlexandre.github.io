# Onde se vota no Piauí

**Tipo:** visualização (piloto) · **Projeto:** eleicoes · **Status:** rascunho, no ambiente de pilotos (L0017) · **Deriva de:** `2026-10_locais-de-votacao`

## Pergunta
Onde ficam os locais de votação do Piauí, e quantos eleitores votam em cada lugar? Piloto para testar o componente
`pontos_agrupados` no hospedeiro Visualização.

## Dados
Recorte publicado do painel "Onde o 2º turno se decide" (`data/locais/22*.js`): locais de 2026, coordenadas e
eleitores aptos, conferidos com o total oficial de cada cidade (EL0009). Contornos dos Territórios de Desenvolvimento
(malha municipal do IBGE).

## Método e decisões
EL0009 (locais), EL0002/L0001 (municípios). Decisão local: só locais convencionais com coordenada dentro do município;
os demais são contados na nota (lacuna informada). Agrupamento: `labdados.agrupamento`.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/eleicoes/produtos/2026-10_onde-se-vota-pi/src/preparar.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/eleicoes/produtos/2026-10_onde-se-vota-pi
```

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Preparo dos dados e textos | Claude (Claude Code) | piloto de componente | pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
