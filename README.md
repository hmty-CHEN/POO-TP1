# Simulation d'un écosystème proie-prédateur

Projet de TP — **Programmation orientée objet en Python**.

Ce dépôt contient la structure initiale du projet. L'objectif est de
simuler l'évolution d'un petit écosystème composé de proies (lapins) et
de prédateurs (loups) évoluant dans un environnement en grille.

> **État actuel : squelette du projet.**
> Les classes et les méthodes sont déclarées mais **non implémentées**.
> Chaque partie à compléter est signalée par un commentaire `TODO`.

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

## Arborescence

```text
simulation-ecosysteme-poo/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── animal.py
│   ├── proie.py
│   ├── predateur.py
│   ├── lapin.py
│   ├── loup.py
│   ├── environnement.py
│   └── simulation.py
├── tests/
│   ├── __init__.py
│   ├── test_animal.py
│   └── test_environnement.py
└── docs/
    ├── conception.md
    └── diagramme-uml.md
```

### Rôle des fichiers

| Fichier | Responsabilité |
| --- | --- |
| `src/animal.py` | Classe abstraite commune à tous les animaux. |
| `src/proie.py` | Comportements communs aux proies. |
| `src/predateur.py` | Comportements communs aux prédateurs. |
| `src/lapin.py` | Proie concrète (déplacement, fuite). |
| `src/loup.py` | Prédateur concret (déplacement, chasse). |
| `src/environnement.py` | Gestion de la grille et des animaux (composition). |
| `src/simulation.py` | Orchestration des tours et des statistiques. |
| `main.py` | Point d'entrée du programme. |
| `tests/` | Tests unitaires (`unittest`). |
| `docs/` | Rapport de conception et diagramme UML. |

---

## Prérequis

- Python 3.10 ou supérieur.
- Aucune dépendance externe (bibliothèque standard uniquement).

---

## Exécution

```bash
python main.py
```

## Tests

```bash
python -m unittest
```

---

## Hiérarchie prévue des classes

```text
        Animal (abstraite)
        ├── Proie
        │   └── Lapin
        └── Predateur
            └── Loup

Environnement  ◆── Animal      (composition)
Simulation     ── Environnement
```

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

## Répartition suggérée

- [ ] `Animal` : attributs communs, énergie, âge, vivant.
- [ ] `Proie` / `Predateur` : comportements spécifiques.
- [ ] `Lapin` / `Loup` : implémentations concrètes.
- [ ] `Environnement` : grille, ajout, suppression, un tour.
- [ ] `Simulation` : populations, boucle, statistiques.
- [ ] Tests unitaires.
- [ ] Diagramme UML.
- [ ] Rapport de conception.

---

## Livrables attendus

- le code Python complet ;
- le diagramme UML ;
- les tests unitaires ;
- un court rapport de conception ;
- une démonstration de la simulation.
