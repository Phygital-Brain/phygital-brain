Conhecimento que se vai juntando com o tempo: decisões, pesquisa, candidaturas e o arquivo.

## Onde guardar

| Conteúdo | Vai para |
|---|---|
| Uma decisão com o seu porquê, ou uma análise de uma coisa de fora (app, site, curso, concorrente) | `decisions/YYYY-MM-DD-{title}.md` |
| Pesquisa (mercado, tendências, opções) | `research/{topic}.md` |
| Candidaturas: empregos, bolsas, prémios, concursos (criado na primeira vez que for preciso) | `applications/{name}/` |
| Perfis da concorrência (criado na primeira vez que for preciso) | `competitors/{name}.md` |
| Dinheiro: faturas, impostos, pagamentos. Privado | `finances/` |
| Decisões arquivadas | `archive/decisions/` |
| Pesquisa acabada ou desatualizada | `archive/research/` |
| Projetos acabados | `archive/{name}/` |
| Notas de reuniões | `decisions/` se daí saiu uma decisão, senão a nota desse dia em `Daily/`. Sugere uma pasta de reuniões só quando houver muitas. |

## Bloco de informação (frontmatter)

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
- `status`: vê abaixo para as decisões e as candidaturas. Todo o resto: `active` ou `closed`.
- `tags`: o tipo, depois o tema.
- Opcional: `project`, `deadline`, `description` (uma frase, entre aspas, na última linha).

## Notas de decisão

Põe sempre o porquê: quem esteve envolvido, o que levou à decisão, o que se ganhou e o que se perdeu. Usa `> [!important]` para a decisão em si e `> [!warning]` para os riscos conhecidos.

As decisões também têm `updated:` logo a seguir a `date:`. `date` é quando foi criada, `updated` é a última vez que foi revista ou alterada.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (ainda a ser decidida ou trabalhada), `waiting` (à espera de outra pessoa), `paused`, `closed`.
- Uma decisão com `updated` de há mais de 30 dias precisa de revisão. O Organizador assinala-a até {Name} a manter, fechar ou arquivar (qualquer uma destas muda `updated` para esse dia).
- Uma decisão só passa para `archive/decisions/` quando {Name} disser.

## Candidaturas

Uma pasta por candidatura: `applications/{name}/`, com um `README.md` que tem o prazo, o link, o estado e o que foi enviado. Os outros ficheiros (respostas, carta de motivação) ficam ao lado.

- `status`: `draft`, `submitted`, `accepted`, `rejected` ou `withdrawn`.
- Guarda as respostas em markdown. PDFs grandes e apresentações ficam fora do cérebro: faz um resumo deles numa nota.

## Regras

- A pesquisa é neutra por defeito (regra geral 23).
- Passa a pesquisa ultrapassada para `archive/research/` em vez de a apagar.
- `finances/` é privada e está na lista do `.claudeignore`. Só a abres quando {Name} pedir um ficheiro concreto (regra geral 8).
