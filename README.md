# Alexandre Cajazeira — portfólio

Página pessoal publicada em <https://cajazeiraalexandre.github.io/> (GitHub Pages, a partir da raiz deste repositório).

## Estrutura

| Caminho | O que é |
|---|---|
| `index.html` | a página (gerada — não editar à mão) |
| `fonte/perfil.yaml` | dados públicos, seções (pesquisa, palestras, extensão…), trajetória e formação |
| `fonte/trabalhos.yaml` | trabalhos anteriores (reportagens, visualizações, padrões de dados) |
| `fonte/template.html` | layout da página |
| `gerar.py` | monta `index.html` a partir de `fonte/` |
| `assets/` | foto e `tokens.css` (cores, fontes e tamanhos) |
| `palestras/` | slides de palestras em HTML |

## Atualizar

```bash
pip install pyyaml
# edite fonte/perfil.yaml ou fonte/trabalhos.yaml
python gerar.py
```

Seções sem itens não aparecem na página. Links oficiais fora do ar ficam guardados em `link_suspenso`
(em `trabalhos.yaml`) ou comentados (em `perfil.yaml`) até voltarem — por exemplo, páginas do gov.br
desativadas no período eleitoral de 2026.

## Licença

Código (`gerar.py`, `fonte/template.html`): MIT. Textos, foto e slides: direitos reservados aos autores
(a palestra de 30/09/2026 é em coautoria com Gabriel Bizerril).
