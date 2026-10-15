# Interpolação entre conjuntos de polígonos

**Tipo:** nota-tecnica (variante interativa) · **Projeto:** metodos-e-recursos · **Status:** rascunho 0.2 (protótipo em avaliação; 0.1 nos pilotos)

## Pergunta
Como animar, de forma automática e suave, a passagem entre dois mapas compostos por vários polígonos que se dividem, se
fundem, surgem e desaparecem? Página interativa e bilíngue (PT/EN) do artigo de Ramos, Santos e Cavalcante Neto
(SIBGRAPI 2019, doi:10.1109/SIBGRAPI.2019.00027), com o algoritmo reimplementado passo a passo, o código ao lado do texto
e a opção de testar com shapefiles ou GeoJSON próprios.

## Dados
| Dataset | Versão | Fonte original |
|---|---|---|
| — (casos sintéticos) | `data/casos.json`, gerado por `analise/casos_sinteticos.py` (seeds fixas) | formas desenhadas para reproduzir a situação das Figs. 7, 9, 10 e 11 do artigo |
| `geobr.municipios_historicos` | malhas simplificadas 1991, 2000, 2010, 2022 (manifesto) | Ipea/geobr, a partir do IBGE |
| `pi.territorios_desenvolvimento` | 2017 | Lei 6.967/2017 (lista da Wikipédia, revisão fixada) |
| `mapbiomas.alerta_desmatamento` | consulta de 2026-10-15 (base inteira: 542.543 alertas, padronizada) | MapBiomas Alerta, CC BY 4.0 |

Caso real (seção 7): Território Serra da Capivara, 1991 → 2000 e 2010 → 2022 (controle), gerado por
`analise/caso_municipios.py`. Limites estaduais dos EUA (Fig. 9 real): não confirmados.

## Método e decisões
- **MR0001**: correspondência (D1, padrão do artigo com seletor), semente do Voronoi (D2), fragmentos (D3, provisório),
  buracos (D4, **em aberto**), surgir/desaparecer pelo centroide (D5), flubber (D6; todo o código em JS), projeção (D7),
  medidas e eventos (D8, em avaliação), casos de teste (D9).
- **L0002** (autocontido; exceção registrada no MR0001 D6: cálculo só em JS, sem espelho em Python) e **L0003** (componentes e bloco de metodologia).
- Decisão local: todos os casos, inclusive os arquivos do leitor, são levados a um quadro 0–100 (mesma escala nos dois
  conjuntos) antes do algoritmo, para que raio, rótulos e segmentos do flubber tenham a mesma escala em qualquer caso.

## Como reproduzir
```bash
# a partir da raiz do laboratório
python projetos/metodos-e-recursos/analise/gerar_interpolacao.py      # casos + index.html
python -m pytest tests/test_metodos_interpolacao.py                    # testes no Chrome headless
python projetos/metodos-e-recursos/analise/explorar_sementes_voronoi.py  # números do MR0001 (D2, D3)
```
Edite `src/` (algoritmo em `src/interpolacao.js`, página em `src/app.js`, textos em `src/textos.yaml`), nunca o
`index.html`.

## Uso de IA
| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Leitura do artigo e proposta de método | Claude (Anthropic), Claude Code | resumir o artigo, identificar lacunas (D1–D9) e propor opções | decisões do pesquisador em 2026-10-15 (MR0001) |
| Teste das regras de semente | Claude, Claude Code | escrever e rodar `analise/explorar_sementes_voronoi.py` (casos sintéticos) | números a conferir pelo pesquisador |
| Reimplementação e página | Claude, Claude Code | escrever `src/interpolacao.js`, `src/app.js`, textos PT/EN, casos sintéticos e testes | protótipo em avaliação; revisão final pendente |
| Levantamento de literatura (seção 9) | Claude, busca web | localizar trabalhos posteriores a 2019 | referências marcadas "a conferir" em `src/referencias.yaml` |

A responsabilidade pelo conteúdo é do pesquisador (Portaria CNPq nº 2.664/2026).

## Licença
Código: MIT · Dados derivados: CC BY 4.0
