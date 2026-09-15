# Rapport de conception

> Document à compléter au fil du projet. Il servira de base à la
> soutenance orale.

## 1. Problématique

Comment concevoir un programme orienté objet capable de représenter et
de simuler un écosystème dans lequel différents types d'animaux
interagissent ?

## 2. Analyse du problème

- Acteurs : proies (lapins) et prédateurs (loups).
- Environnement : grille avec largeur et hauteur.
- Actions : se déplacer, vieillir, consommer de l'énergie, chasser,
  fuir, se reproduire, mourir.

## 3. Répartition des responsabilités

| Classe | Responsabilité | À compléter |
| --- | --- | --- |
| `Animal` | État commun et comportements partagés | |
| `Proie` | Comportements des proies | |
| `Predateur` | Comportements des prédateurs | |
| `Lapin` | Implémentation concrète d'une proie | |
| `Loup` | Implémentation concrète d'un prédateur | |
| `Environnement` | Composition : grille + collection d'animaux | |
| `Simulation` | Orchestration et statistiques | |

## 4. Choix d'héritage

À compléter : pourquoi `Lapin` hérite de `Proie`, pourquoi `Loup` hérite
de `Predateur`, et pourquoi `Animal` est abstraite.

## 5. Polymorphisme

À compléter : montrer un exemple où `animal.se_deplacer()` est appelé sur
une collection hétérogène sans `isinstance`.

## 6. Encapsulation

À compléter : expliquer pourquoi l'énergie est modifiée via
`perdre_energie` / `gagner_energie` plutôt que directement.

## 7. Composition

À compléter : décrire la relation entre `Environnement` et les animaux.

## 8. Difficultés rencontrées

À compléter.
