# Buscas no Google na campanha presidencial de 2026

**Tipo:** painel · **Projeto:** eleições · **Status:** piloto (versão de teste) · **Versão:** 0.1 (20/10/2026)

## Pergunta
Nas buscas do Google sobre o 2º turno presidencial de 2026, quem está sendo mais buscado entre Flávio Bolsonaro e Lula,
quais temas aparecem junto com cada nome e com qual nome cada tema aparece mais — nas últimas 4 horas, 24 horas, 7 dias
ou desde 16/08 (início da campanha). Busca mede atenção, não intenção de voto.

## O que a página mostra
1. **Quem está sendo mais buscado** — parte de cada nome nas buscas pelos dois (média do Google no período ÷ soma das
   duas), a série no tempo e a divisão por estado (Brasil) ou cidade (Piauí).
2. **Temas associados a cada nome** — peso de cada tema nas buscas feitas junto com o nome e as buscas que mais cresceram.
3. **Com qual nome cada tema aparece mais** — buscas que juntam o tema e o nome ("corrupção flávio" × "corrupção lula").
4. **Em alta no Google** — buscas em alta ligadas à eleição, com as notícias que o Google liga a elas.
5. **Outros grupos de busca** — campanha, serviço ao eleitor, esquerda e direita, economia, integridade e segurança.

## Dados
| Base | Fonte |
|---|---|
| Interesse no tempo, por região e buscas relacionadas | Google Trends, página Explorar (coleta por programa, com pausa de ~10 s entre pedidos) |
| Buscas em alta (Brasil e Piauí) | Google Trends, feed público RSS |

O Google Trends é dado de uma empresa privada, não oficial. O índice vai de 0 a 100 e é **relativo à consulta**,
calculado sobre uma amostra: só compara termos da mesma consulta e pode variar um pouco entre coletas. Quando o Google
não informa um valor ("<1" ou sem dado), a página mostra lacuna, nunca zero. Cada coleta é guardada com data e hora.

## Método
- **Parte nas buscas:** média do Google no período para cada termo ÷ soma das médias da mesma consulta.
- **Peso de cada tema:** cada busca relacionada a um nome entra num tema por uma lista de palavras (sem acento, palavra
  inteira); a que cita o adversário e não cai em outro tema vai para "Disputa, pesquisas e debate"; a que não cai em
  nenhum, para "Outros assuntos". Peso = soma do índice das buscas do tema ÷ soma de todas.
- **Tema × nome:** média do Google para "<tema> <nome>" ÷ soma das duas; abaixo de uma soma mínima, o tema aparece como
  "poucas buscas".
- Listas de palavras, termos sugeridos e regras de classificação são **propostas em teste**, marcadas na página.

## Limitações
- A coleta usa os mesmos endereços que a página do Google usa, não uma API pública: o Google pode recusar pedidos (as
  recusas ficam registradas e são avisadas na página) ou mudar o formato sem aviso.
- "flávio" também pega buscas sobre outros Flávios; junto de um tema, quase sempre é Flávio Bolsonaro.
- As buscas relacionadas são escritas pelas pessoas: podem trazer acusações, boatos e erros de grafia. Mostram o que se
  procurou, não se é verdade.
- Esta página é um retrato da última coleta; não se atualiza sozinha.

## Uso de IA
A pergunta, o recorte (2º turno presidencial; Brasil e Piauí; desde 16/08 e janelas curtas), os temas acompanhados, a
decisão de coletar os dados e desenhar com os componentes do laboratório e a síntese da página em torno de quem é mais
buscado e dos temas de cada nome são do pesquisador, assim como os modelos e as regras do laboratório. Dentro desse
quadro, Claude (Claude Code, Anthropic) testou o acesso ao Google Trends, propôs opções de coleta e de medida, sugeriu
termos e listas de palavras (marcados como proposta), escreveu os scripts de coleta e a página e redigiu os textos
(Portaria CNPq nº 2.664/2026). A verificação humana das propostas está em andamento. A responsabilidade pelo conteúdo é
do pesquisador; a IA não é autora.

## Licença
Código: MIT · Dados derivados: CC BY 4.0. Fonte dos dados: Google Trends.
