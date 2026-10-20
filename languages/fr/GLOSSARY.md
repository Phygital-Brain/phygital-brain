# Glossaire français (fr)

Les mots choisis pour la version française de Phygital Brain, et pourquoi.

## Registre

- **« vous »** partout où le produit parle à la personne (formulaires, messages, règles, Gardien du cerveau). C'est ce qu'utilisent la plupart des apps grand public en France (Apple, Google, Notion, la plupart des banques et des services). Les règles écrites pour l'agent sont aussi au « vous » (« Lisez », « Demandez d'abord »).
- **« tu »** seulement dans les phrases que la personne dit à son agent (« fais le bilan de mon cerveau », « prépare-moi pour Claire », et l'exemple de consignes `instructions_example`). On tutoie naturellement un assistant, comme on dit « Dis Siri ».
- Pas de pronom genré pour la personne : on répète {Name} ou on tourne la phrase autrement (« comment {Name} veut que son agent travaille »). Quelques mots de formulaire restent au masculin par défaut (« doué », « concentré », « Freelance ou créateur »).

## Typographie

- Espace insécable avant `:` `;` `?` `!`, et à l'intérieur des guillemets « ».
- Guillemets « » pour les citations et les phrases déclencheurs en français. Les déclencheurs anglais gardés à côté sont entre guillemets droits "...".
- Apostrophe droite `'`.
- Jamais de tiret long (cadratin).

## Noms des fonctions

| Anglais | Français |
|---|---|
| Brain Keeper | Gardien du cerveau |
| morning brief | point du matin |
| meeting prep | préparation de réunion |
| thinking tools | outils de réflexion |
| check-up | bilan |
| Writing Check | Contrôle d'écriture |
| second brain | second cerveau |
| your agent | votre agent |
| Phygital Brain | Phygital Brain (inchangé) |

## Dossiers principaux

| Anglais | Français | Pourquoi |
|---|---|---|
| About | Profil | « À propos » contient une espace et un accent en tête, et « Profil » dit bien « l'essentiel sur vous » |
| Daily | Journal | Le mot courant pour des notes datées, une par jour |
| Projects | Projets | |
| Relationships | Relations | |
| Memory | Mémoire | |
| Library | Bibliothèque | |
| Skills | Compétences | Le nom utilisé en français pour les « skills » d'un agent |

## Sous-dossiers et notes

| Anglais | Français |
|---|---|
| Clients, Collaborators, Team, Partners | Clients, Collaborateurs, Équipe, Partenaires |
| decisions, research, finances, archive | décisions, recherches, finances, archives |
| applications, competitors | candidatures, concurrents |
| notes, briefs, drafts, ideas, feedback, assets | notes, briefs, brouillons, idées, retours, médias |
| prompts, templates, frameworks | prompts, modèles, méthodes |
| brain-keeper, morning-brief, meeting-prep | gardien-du-cerveau, point-du-matin, préparation-réunion |
| thinking, import, connected-apps, reports | réflexion, import, apps-connectées, rapports |
| me, goals, business, services, customers | moi, objectifs, activité, offres, clientèle |
| pain-points, brand, tools, cv, biography | difficultés, marque, outils, cv, biographie |
| tasks, _Leads | tâches, _Prospects |
| daily, check-up, queue, PAUSED | quotidien, bilan, à-traiter, EN-PAUSE |

- `customers` devient `clientèle` pour ne pas se confondre avec le dossier `Clients`.
- `services` devient `offres` : le fichier contient services, produits et offres.
- `briefs` et `prompts` restent tels quels : ce sont les mots qu'on utilise en France dans le métier.

## Termes fixés

| Anglais | Français |
|---|---|
| info block (frontmatter) | bloc d'infos |
| daily note | note du jour |
| compiled-truth format | format « vérité en haut » |
| evidence | preuves |
| lead | prospect |
| New / Keep warm (dans `_Leads.md`) | Nouveaux / À relancer |
| run (du Gardien) | passage |
| queue | file (dans le texte), à-traiter (nom du fichier) |
| Needs {Name} / To fix / Next folder / Last run | Pour {Name} / À corriger / Dossier suivant / Dernier passage |
| safe fixes | corrections sans risque (la valeur `safe fixes` reste en anglais) |
| dry run | simulation |
| callout | encadré |
| orphan note | note orpheline |
| Knowledge Routing | Où ranger chaque info |
| Session Startup | Au début de chaque discussion |
| Backups and Undo | Sauvegardes et annulation |
| Status and next step | Où on en est et prochaine étape |
| What it is / How it runs / Where things are | De quoi il s'agit / Comment ça tourne / Où trouver quoi |
| {Name}'s Rules | Les règles de {Name} |
| Document Voice / Anti-Patterns / Work Guidelines | Le ton des notes / À ne pas faire / Façon de travailler |
| cloud drive | cloud |
| chat | discussion |
| (from email) / (from calendar) | (par e-mail) / (d'après l'agenda) |
| read from (an app) | consulter |
| pause / resume the Brain Keeper | mettre en pause / réactiver (pas « relancer », trop proche de « lancer ») |
| {n} things need you | {n} point(s) vous attendent |

## Noms d'exemple

Ana Costa devient Léa Martin, Marta devient Claire, João devient Hugo, Lia devient Inès, Lisbonne devient Lyon. `[[Ana]]` devient `[[Léa]]` dans les modèles.

## Points à relire

- La section « Langue » du `CLAUDE.md` racine dit, comme la version anglaise, que les noms de dossiers, de fichiers et les `[[liens]]` restent exactement tels que ces règles les écrivent.
- `Skills` devient `Compétences`, le mot utilisé en français pour les « skills » d'un agent. Risque de confusion avec les compétences de la personne (formulaire 1, `cv`) : à confirmer par un relecteur natif.
- Les commentaires ADAPTING restent en anglais et citent des titres anglais (« Connected », « None yet. », « Morning Brief row »). Leurs équivalents français sont « Connectées », « Aucune pour l'instant. » et la ligne « Point du matin ».
