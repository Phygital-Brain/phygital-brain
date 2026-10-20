---
type: skill
status: active
tags: [brain-keeper, check-up]
---

Le bilan du Gardien du cerveau : un tour complet de tout le cerveau, quand {Name} le demande. Rien ne change tant que {Name} n'a pas dit oui. (Le rangement quotidien est dans `daily.md`.)

Déclencheur : « fais le bilan de mon cerveau », « range mon cerveau », « bilan du cerveau », "check up my brain", "tidy my brain", "brain check-up", ou l'équivalent en {Language}.

## 1. Regarder (sans rien changer pour l'instant)

Parcourez tout le dossier et listez les problèmes dans ces groupes :

- **Liens cassés** : des `[[liens]]` vers des notes qui n'existent pas. Ne les réparez jamais en créant une note vide : la vraie note est peut-être encore en cours de synchronisation (règle 28 du fichier racine).
- **Notes orphelines** : des notes vers lesquelles aucune autre note n'a de lien.
- **Notes vides ou presque**, et les textes provisoires oubliés (`[name]`, `TBD`).
- **Mal rangé** : des fichiers à la racine du dossier (sauf `CLAUDE.md`, `.claudeignore`, `.backups/` et le fichier de règles d'une ligne d'un autre agent, comme `AGENTS.md`), des notes qui ne correspondent pas au tableau de rangement de leur dossier.
- **Tableaux de rangement pas à jour** : un `CLAUDE.md` liste des fichiers ou des dossiers qui n'existent pas, ou en oublie qui existent (les lignes marquées « créé à la première utilisation » sont normales).
- **Blocs d'infos** : absents ou incomplets, par rapport au `CLAUDE.md` du dossier. Pas de `status:`, moins de 2 `tags:`, une note de projet sans `project:`, des tags de note du jour hors de la liste fixe.
- **Projets à l'arrêt** : aucune mise à jour depuis 60 jours ou plus. Proposez une mise à jour du statut, `paused`, ou l'archivage.
- **Objectifs à la dérive** : des objectifs de `About/goals.md` sans aucun projet actif.
- **Décisions à revoir** : `updated` date de plus de 30 jours et le statut n'est pas `closed`.
- **Relations anciennes** : `status: active` mais `last-contact` date de plus de 12 mois. Proposez `dormant`.
- **Vieilles tâches** : des tâches en cours dans `Daily/tasks.md` ajoutées il y a plus de 30 jours.
- **Doublons** : les mêmes faits dans plusieurs notes, ou deux notes pour la même personne ou la même entreprise.
- **Vérité pas à jour** : des pages Profil ou Relations où de vieilles mises à jour enterrent l'état actuel (règle 17 du fichier racine).
- **Règles contradictoires** : des règles du `CLAUDE.md` racine qui se contredisent.
- **Confidentialité** : des mots de passe, des clés ou des numéros privés dans des notes ordinaires (règles 25 et 26 du fichier racine). Indiquez la note, jamais la valeur.
- **Écriture** : des tirets longs et des tics du Contrôle d'écriture dans les notes.

## 2. Faire le rapport

Une liste courte, avec des mots simples, groupée comme ci-dessus. Pour chaque problème : la note, ce qui ne va pas, la correction que vous proposez. Mettez d'abord les corrections simples et sans risque (tirets longs, tags manquants, lignes des tableaux de rangement).

## 3. Corriger seulement ce qui est validé

Avant la première correction, sauvegardez chaque fichier que vous allez modifier (« Sauvegardes et annulation » dans le `CLAUDE.md` racine).

Demandez (avec des choix cliquables si possible) : **Corriger tout ce qui est sans risque**, **Une par une**, **Juste le rapport**.

- Ne supprimez et ne déplacez jamais rien sans vérifier les liens et sans un oui clair (règle 21 du fichier racine).
- Dans le doute, archivez au lieu de supprimer.
- Notez une ligne dans la note du jour de `Daily/` : ce qui a été vérifié et corrigé.
