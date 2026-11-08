# Projeto final: o seu site com várias páginas

**Tipo:** didatico · **Projeto:** programacao-web-didatico · **Status:** rascunho (piloto 0.7) ·
**Endereço:** <https://cajazeiraalexandre.github.io/ifpi-2026-2/projeto-final-web/>

## Pergunta
O que é o projeto final do 4º bimestre de Desenvolvimento Web Front-End (1º ano integrado, IFPI/SRN), como as aulas
restantes se dividem em etapas, como salvar o trabalho, como a nota é composta e como enviar.

## Conteúdo
Página única para apresentar em sala (botão **Modo apresentação**, tecla P ou `#apresentacao` no endereço: slides 16:9
clonados da própria página) e para consulta dos alunos: o que é, calendário do bimestre (09/11 a 18/12), plano da
primeira aula com modelo da ficha do tema, rotina de salvar no Google Drive (zip numerado a cada aula, pasta
compartilhada com o professor), avaliação (site 7,0 em três blocos; apresentação 3,0 por critérios), o que não pode,
entrega e roteiro da apresentação, prévia do formulário de envio e dúvidas. Sem dados (ADR PW0001).

## Decisões
Registradas na seção 6 de `docs/2026-11-05_projeto-final-proposta.md` do projeto: calendário do professor; recuperação
por prova; lista em quatro blocos sem "Base/Completo"; apresentação com 30% da nota e critérios subjetivos; página sem
nada para preencher; formulário de envio na ordem do roteiro; salvamento no Google Drive; pasta compartilhada com o
professor desde a primeira aula; modo apresentação.

**Decisões locais (professor, 2026-11-08):**
- Em tela larga (mais de 900 px e mais larga que alta), sem trecho no endereço, a página **abre como slides**; celular,
  baixa visão ou endereço com trecho (`#pagina`, `#calendario`, `#acesso=…`) abrem a página. "Ver como página" (ou Esc)
  sai dos slides e grava `#pagina`, para a próxima abertura ser a página. O botão "Modo apresentação" fica numa barra
  própria no alto, fora do menu de conteúdos.
- **Baixa visão**, com o mesmo desenho do caderno de HTML e CSS: texto de 125% a 200%, contraste alto, fundo escuro
  opcional, uma coluna, foco visível, links sublinhados; guardada no navegador e no endereço
  (`#acesso=baixa-visao&escala=150&tema=escuro`), que o professor pode enviar pronto. Nos slides, a baixa visão mantém o texto ampliado e o contraste alto; o slide
  rola em vez de encolher (aviso "role para ver mais"; Espaço e PageDown descem até o fim antes de passar).

**Decisão local:** a página é escrita à mão, sem montagem por script nem YAML (diferente do caderno), porque é um
documento de uma aula e de um bimestre. O link do formulário de envio entra na variável `LINK_FORMULARIO` do script.

## Uso de IA
A proposta do trabalho final, o calendário, os critérios, os pesos, as regras e todas as decisões são do professor
Alexandre Cajazeira Ramos, que pediu e revisou cada versão; o formato segue os modelos e as regras do laboratório e do
projeto (ADR PW0001). Dentro desse quadro, o assistente executou (Portaria CNPq nº 2.664/2026; a responsabilidade pelo
conteúdo é do professor e a IA não é autora):

| Etapa | Ferramenta | Finalidade | Revisão humana |
|---|---|---|---|
| Redação a partir da proposta de 2026-11-05 e do calendário | Claude (Claude Code) | organizar o texto para os alunos e distribuir as etapas pelas aulas | professor, versões 0.1 a 0.7 (2026-11-08) |
| Página HTML e modo apresentação | Claude (Claude Code) | montar a página autocontida e os slides | professor; conferência técnica automática (marcação, script, largura no celular, slides) |

## Licença
Código: MIT · Textos: CC BY 4.0
