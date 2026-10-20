Conhecimento que se acumula com o tempo: decisões, pesquisas, candidaturas e o que foi arquivado.

## Onde guardar

| Conteúdo | Vai para |
|---|---|
| Decisão com o raciocínio, ou estudo de uma coisa de fora (app, site, curso, concorrente) | `decisions/YYYY-MM-DD-{title}.md` |
| Pesquisa (mercado, tendências, opções) | `research/{topic}.md` |
| Candidaturas: vagas, bolsas, prêmios, editais (criado no primeiro uso) | `applications/{name}/` |
| Perfis de concorrentes (criado no primeiro uso) | `competitors/{name}.md` |
| Dinheiro: notas fiscais, impostos, pagamentos. Privado | `finances/` |
| Decisões arquivadas | `archive/decisions/` |
| Pesquisas terminadas ou desatualizadas | `archive/research/` |
| Projetos terminados | `archive/{name}/` |
| Anotações de reunião | `decisions/` se saiu uma decisão dela, senão a nota do `Daily/` daquele dia. Sugira uma pasta de reuniões só quando houver muitas. |

## Bloco de informações (frontmatter)

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`: `decision`, `research`, `application`, `competitor`.
- `date`: a data em que a nota foi escrita.
- `status`: veja abaixo para decisões e candidaturas. Todo o resto: `active` ou `closed`.
- `tags`: o tipo, depois o assunto.
- Opcional: `project`, `deadline`, `description` (uma frase, entre aspas duplas, na última linha).

## Notas de decisão

Sempre inclua o porquê: quem participou, o que motivou, que troca foi feita (o que se ganhou e o que se perdeu). Use `> [!important]` para a decisão em si e `> [!warning]` para os riscos conhecidos.

As decisões também levam `updated:` logo depois de `date:`. `date` é quando ela foi criada, `updated` é a última vez que foi revista ou mudou.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (ainda sendo decidida ou trabalhada), `waiting` (esperando outra pessoa), `paused`, `closed`.
- Uma decisão com `updated` de mais de 30 dias precisa de revisão. O Guardião do Cérebro aponta essa decisão até {Name} manter, fechar ou arquivar (cada uma dessas coloca o dia em `updated`).
- Uma decisão vai para `archive/decisions/` só quando {Name} disser.

## Candidaturas

Uma pasta por candidatura: `applications/{name}/`, com um `README.md` que guarda o prazo, o link, a situação e o que foi enviado. Os outros arquivos (respostas, carta de apresentação) ficam ao lado.

- `status`: `draft`, `submitted`, `accepted`, `rejected` ou `withdrawn`.
- Guarde as respostas em markdown. PDFs e apresentações grandes ficam fora do cérebro: resuma numa nota.

## Regras

- Pesquisa é neutra por padrão (regra 23 da raiz).
- Mova pesquisas superadas para `archive/research/` em vez de apagar.
- `finances/` é privada e está listada no `.claudeignore`. Abra só quando {Name} pedir um arquivo específico (regra 8 da raiz).
