# Simulation d'un écosystème proie-prédateur

Projet de TP — **Programmation orientée objet en Python**.

Ce dépôt contient l'avancement progressif du TP. Les exercices 1 à 6 portent
uniquement sur une classe simple `Lapin`.

> **État actuel : exercices 1 à 6 réalisés.** L'héritage, les loups et
> l'environnement seront ajoutés dans les étapes suivantes.

---

## Objectifs pédagogiques

Ce projet sert à mettre en pratique :

- les classes et les objets ;
- les attributs et les méthodes ;
- les constructeurs ;
- l'héritage ;
- l'abstraction ;
- le polymorphisme ;
- l'encapsulation ;
- la composition ;
- les collections d'objets ;
- les tests unitaires ;
- la modélisation UML.

---

## Arborescence actuelle

```text
simulation-ecosysteme-poo/
├── lapin.py
├── main.py
├── rapport.html
├── traduction-rapport.md
└── docs/
    └── uml-exercices-1-a-6.md
```

### Rôle des fichiers

| Fichier | Responsabilité |
| --- | --- |
| `lapin.py` | Classe `Lapin` et quelques appels de vérification. |
| `main.py` | Création de cinq lapins et manipulation de la liste. |
| `rapport.html` | Rapport de cours en français. |
| `traduction-rapport.md` | Traduction chinoise du rapport. |
| `docs/` | Diagramme UML de l'étape actuelle. |

---

## Prérequis

- Python 3.10 ou supérieur.
- Aucune dépendance externe (bibliothèque standard uniquement).

---

## Exécution

```bash
python main.py
```

## Vérification

```bash
python lapin.py
```

---

Les appels de vérification sont placés dans `lapin.py`.

---

## Organisation du travail en équipe

1. Créer une branche par fonctionnalité :
   ```bash
   git checkout -b fonctionnalite/ma-partie
   ```
2. Faire des commits courts et explicites (en français).
3. Pousser la branche puis ouvrir une *pull request*.
4. Demander une relecture avant de fusionner dans `main`.

Merci de **ne pas travailler directement sur `main`**.

---

## Étapes suivantes

- [x] Exercices 1 à 6 : classe simple `Lapin`.
- [ ] Exercices suivants : héritage et classe `Animal`.
- [ ] Ajouter progressivement `Loup`, `Environnement` et `Simulation`.

---

## Livrables attendus

- le code Python complet ;
- le diagramme UML ;
- les tests unitaires ;
- un court rapport de conception ;
- une démonstration de la simulation.
