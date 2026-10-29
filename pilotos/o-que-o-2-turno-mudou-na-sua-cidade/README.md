# Onde o 2º turno para presidente foi decidido em sua cidade?

**Tipo:** story (declarativo, L0015; modo apresentação em tela larga) · **Projeto:** eleicoes · **Status:** rascunho (0.1, para
revisão do pesquisador) · **Origem:** sequência de `eleicoes/2026-10_2-turno-na-sua-cidade@1.0` (linhagem, L0009): os mesmos
locais, agora 1º × 2º turno de 2026 · **Publicação prevista:** repositório `eleicoes`, em teste sem divulgação
(`o-que-o-2-turno-mudou-na-sua-cidade`); publicar é decisão do pesquisador.

## Pergunta
Onde, na sua cidade, Lula cresceu do 1º para o 2º turno de 2026, e de onde vieram esses votos (abstenção, brancos e
nulos, outras candidaturas)? Em quais locais a liderança mudou de mão? Perspectiva de Lula, o vencedor, com Flávio
Bolsonaro sempre na mesma régua (briefing de 2026-10-29).

## Cartões (roteiro v2, validado em 2026-10-29 — propostas 1 + 2 + 3 num arco só, L0018)
Capa · placar da cidade (Lula, Flávio e abstenção nos dois turnos; estado e Brasil na nota) · a conta dos votos
(identidade contábil, colunas ligadas) · local a local (crescimento de Lula × votos em disputa; cor = quem cresceu mais) ·
onde Lula mais cresceu · Lula × Flávio (enxame pela diferença dos crescimentos) · onde a abstenção caiu (enxame) · onde
outros candidatos foram mais fortes (10 locais, Lula e Flávio do 1º ao 2º turno) · quem liderou em cada turno
(ficou/virou) · mapa (área = votos a mais de Lula; cor = quem cresceu mais) · bairros onde Lula mais cresceu (captação)
· fim. Cartões saem quando a cidade não tem o que mostrar (34 cidades sem local comparável; 3.724 com cartão de bairros).

## Dados
Saída de `analise/preparar_2_turno_decidido.py`: `data/locais/<IBGE>.js` (tabela de locais + dados e textos de cada
cartão), `data/municipios.json` e `analise/relatorio_qualidade_2_turno_decidido.json`.
- 1º turno por local: recorte conferido de `2026-10_locais-de-votacao` (os mesmos 83.514 locais comparáveis do story de origem).
- 2º turno por local: `votacao_secao_2026_BR` e `detalhe_votacao_secao_2026` na versão de 26/10/2026 (com o 2º turno),
  baixada ao lado da de 05/10 sem apagá-la (resposta 2A): o 1º turno é idêntico nas duas (3.800.511 linhas, zero
  diferença). Seção → local pelo cadastro de 2026, como no 1º turno (497.897 seções, todas ligadas; em 810 o detalhe do
  2º turno indica outro número de local, e vale o cadastro).
- Totais da cidade, do estado e do Brasil: cópias locais da API de resultados do TSE (1º e 2º turno).
- Conferência (tolerância zero): Σ de todas as seções do município × API do 2º turno em Lula, Flávio, brancos, nulos,
  aptos e abstenções — 5.570 municípios, nenhuma divergência; a conta dos votos fecha em todas as cidades; nenhum local
  comparável ficou sem 2º turno; 4.213 locais mudaram de líder.

## Método e decisões (pesquisador, 2026-10-29)
- EL0009 (mesmos locais do original), EL0003 (válidos), EL0010 (rótulo pelo nome), EL0002/L0001 (municípios).
- M1 votos em disputa = aptos do 1º turno − Lula − Flávio (os números do original); aptos dos dois turnos na dica.
- M2 crescimento em p.p. dos válidos e captação (votos a mais ÷ votos em disputa); "perdeu votos" só no absoluto;
  Lula − Flávio = diferença dos crescimentos.
- M3 líder por turno; empate é classe própria, fora das contagens de "virou". M4 abstenção em p.p. dos aptos.
- M5 outras candidaturas = 10 locais com maior fatia no 1º turno (3 ou mais locais). M6 bairros pela captação sobre
  todos os locais comparáveis do bairro; 10 maiores; 3 ou mais bairros.
- M8 o destaque do story de origem não entra ("quem vai ler esse nem se lembra da leitura do original").
- M9 a conta dos votos é identidade contábil: outras + comparecimento a mais + brancos e nulos a menos = votos a mais
  dos dois; a diferença de aptos fica na nota. Não diz de onde cada candidato tirou votos (saldo, não fluxo).
- V1 (dispersão com eixo trocado por cartão) resolvido sem mudar o núcleo: a dispersão principal tem eixo fixo e os
  cartões Lula × Flávio e abstenção usam o enxame (`distribuicao`, componente experimental em story).

## Limites conhecidos (0.1)
- Textos: títulos ≤ 80, textos ≤ 70, notas ≤ 120 em 5.570 cidades, exceto 2 títulos de Vila Bela da Santíssima Trindade
  (nome de 32 letras: capa com 81 e "Lula × Flávio" com 83 caracteres).
- No celular, o texto do cartão aparece numa linha (comportamento do hospedeiro); as frases foram escritas para isso.
- Captura de cada cartão (Chrome sem janela, 430×932 e 1366×800) feita para Teresina; revisão visual do pesquisador pendente.

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python projetos/eleicoes/analise/preparar_2_turno_decidido.py          # dados (~1,5 min; duckdb nos arquivos por seção)
PYTHONPATH=nucleo python -m labdados.viz og projetos/eleicoes/produtos/2026-10_2-turno-decidido-na-sua-cidade   # página e og.png (Chrome)
PYTHONPATH=nucleo:. python -m pytest tests/test_eleicoes_2_turno_decidido.py
```

## Uso de IA
O desenho do produto é do pesquisador — a ideia da sequência, a pergunta, o briefing (respostas 1B, 2A, 3A, 4A, 5A, 6A,
7A, 8A, 9B), a escolha de mesclar as propostas de roteiro 1, 2 e 3, as decisões de método M1 a M9 e as validações —,
assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, tipos de produto,
design system, story declarativo, ADRs), amadurecidos por ele com apoio dos agentes. As propostas de roteiro e o roteiro
ampliam o briefing e seguem os stories já validados pelo pesquisador ("2º turno na sua cidade", "A virada de 2026"). A
tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo é
do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Briefing, bases e propostas de roteiro (2026-10-29) | Claude (Claude Code, Anthropic) | Perguntas do briefing, download e conferência da nova versão dos arquivos por seção, cinco propostas de roteiro | Respostas, escolha da base e dos enxertos pelo pesquisador |
| Método, dados e produto 0.1 (2026-10-29) | Claude (Claude Code, Anthropic) | Proposta de método (M1–M9), script dos cartões com funções testadas, conferência com a API, `viz.yaml`, folha de metodologia, capturas | Método validado pelo pesquisador; conferência automática sem divergência; revisão visual e dos números pendente |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
