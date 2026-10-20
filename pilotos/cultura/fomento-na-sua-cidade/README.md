# O que o fomento à cultura levou à sua cidade (título provisório)

**Tipo:** story (fatias por município) · **Projeto:** cultura · **Status:** rascunho · **Versão:** 0.1 (v0)

## Pergunta
Qual o impacto imediato das políticas de fomento à cultura em seu município e região? (briefing) Lida como: o que a
PNAB, a Lei Paulo Gustavo e a Lei Rouanet levaram à cidade de 2023 a 2026, para quem, por qual ente e comparado com o
orçamento de cultura da prefeitura, a região, o estado e o país. O leitor escolhe a cidade na capa.

## Dados
| Dataset | Uso | Acesso |
|---|---|---|
| `minc.pnab_dados_abertos` | contemplados da PNAB, perfil (Receita, CadÚnico), CNPJ para a cor dos Pontos | aberto |
| `minc.pnab_contemplados` | valores e datas da PNAB (correção pelo IPCA), documentos distintos | restrito, só agregados |
| `minc.lpg_contemplados` | contemplados, valores, perfil e residência da LPG | restrito, só agregados |
| `minc.lpg_painel_utilizacao` | repasse da LPG à prefeitura e ao estado (valor e data) | aberto |
| `minc.salic_api`, `minc.salic_extracoes` | Rouanet: locais de realização e sede do proponente | aberto / restrito, só agregados |
| `minc.pncv_cadastro` | rede de Pontos, fomentados, públicos prioritários, localização pública | restrito; posição só a que o Ponto publica |
| `siconfi.dca_funcao_cultura` | orçamento: função 13 e subfunção 392, 2023–2025 | aberto (API, cópia local) |
| `ibge.*` | Censo 2022, PIB 2022, Regiões Imediatas, REGIC 2018, IPCA, malha municipal | aberto |

## Método e decisões
- Proposta de dados e método validada item a item em 2026-10-16/17: [src/proposta-dados-metodo.md](src/proposta-dados-metodo.md).
- Relatório de qualidade validado em 2026-10-17: [src/relatorio-qualidade.md](src/relatorio-qualidade.md).
- Roteiro validado em 2026-10-17 (v1; v2 com as frases dos casos-limite): [src/roteiro.yaml](src/roteiro.yaml), prancha [roteiro.html](roteiro.html).
- ADRs: L0002, L0004, L0015, L0018, L0019, CN0001, CN0002, CN0003, CN0004, CN0007, CN0009, CN0010.

**Decisões locais (só deste produto):** corte de 10 pessoas para o perfil, com recuo para a Região Imediata e a UF;
faixas de idade comuns às duas leis pela idade; orçamento lado a lado, nunca somado; Pontos no mapa só com a posição
que publicam e dentro do município declarado; cor de fomentado só para o recebimento público (PNAB pelo CNPJ).

## Como reproduzir
```bash
PYTHONPATH=nucleo:. python fontes/siconfi/consultar_dca.py                     # orçamento (cópia local versionada)
PYTHONPATH=nucleo:. python projetos/cultura/analise/cidade_qualidade.py        # relatório de qualidade
PYTHONPATH=nucleo:. python projetos/cultura/analise/cidade_indicadores.py      # tabela por município (fora do git)
PYTHONPATH=nucleo:. python projetos/cultura/produtos/2026-10_qual-o-impacto-imediato-das-politicas-de/src/preparar_story.py
PYTHONPATH=nucleo:. python -m labdados.viz og projetos/cultura/produtos/2026-10_qual-o-impacto-imediato-das-politicas-de
```
As bases restritas do MinC precisam ser recebidas pelo mesmo canal (L0004).

## Uso de IA
O desenho do produto é do pesquisador — pergunta, briefing com o roteiro inicial, recortes, decisões de método e
validações —, assim como os modelos e as especificações do laboratório em que o assistente trabalha (CLAUDE.md, modelos,
ADRs e o story "2º turno na sua cidade", de onde vem o formato por cidade), amadurecidos por ele com apoio dos agentes.
A tabela registra o que a IA executou dentro desse quadro (Portaria CNPq nº 2.664/2026; a responsabilidade pelo conteúdo
é do pesquisador e a IA não é autora).

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Propostas de roteiro | Claude (Claude Code, Anthropic) | ampliar o briefing em cinco caminhos (L0018) | escolha da proposta 1 pelo pesquisador |
| Proposta de dados e método | Claude | organizar opções e recomendações por item (M1–M10, M9b) | validação item a item; decisões próprias em M1, M2, M3, M4 e M9 |
| Fonte nova (Siconfi) | Claude | escrever a consulta e estimar o tamanho da cópia local | autorização da fonte e da cópia |
| Relatório de qualidade | Claude | código de conferência só com agregados | validação dos quatro pontos levantados |
| Indicadores | Claude | código por município, com testes (tests/test_cidade_indicadores.py) | conferência com os números dos exploratórios; faixas de idade decididas pelo pesquisador |
| Roteiro e prancha | Claude | redigir o roteiro da proposta escolhida e gerar a prancha de Teresina | validação do roteiro |
| Página | Claude | programar as fatias por município e a especificação do story | revisão da v0 (pendente) |

## Licença
Código: MIT · Dados derivados: CC BY 4.0
