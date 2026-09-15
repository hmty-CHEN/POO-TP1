# Simulation d'un écosystème proie-prédateur

Projet de TP — Programmation orientée objet en Python.

> État actuel : intégration finale (classes `Proie`, `Predateur`, `Simulation`).

## Arborescence

```text
simulation-ecosysteme-poo/
├── animal.py
├── proie.py
├── predateur.py
├── lapin.py
├── loup.py
├── environnement.py
├── simulation.py
├── visualisation.py
├── main.py
├── test_animal.py
├── test_environnement.py
├── rapport.html
└── traduction-rapport.md
```

| Fichier | Contenu |
| --- | --- |
| `animal.py` | Classe abstraite `Animal`. |
| `proie.py` | Classe abstraite `Proie`. |
| `predateur.py` | Classe abstraite `Predateur`. |
| `lapin.py` | Classe `Lapin`, hérite de `Proie`. |
| `loup.py` | Classe `Loup`, hérite de `Predateur`. |
| `environnement.py` | Classe `Environnement` (composition, tours, statistiques). |
| `simulation.py` | Classe `Simulation` (populations, tours, affichage). |
| `visualisation.py` | Interface graphique tkinter (grille, paramètres, statistiques). |
| `main.py` | Point d'entrée : lance la simulation. |
| `test_animal.py` | Tests unitaires des animaux. |
| `test_environnement.py` | Tests unitaires de l'environnement. |
| `rapport.html` | Rapport de cours en français. |
| `traduction-rapport.md` | Traduction chinoise du rapport. |

## Exécution

```bash
python main.py
python visualisation.py
```

## Tests

```bash
python -m unittest
```

## Organisation du travail

1. Créer une branche par fonctionnalité.
2. Faire des commits courts et explicites.
3. Pousser la branche puis ouvrir une pull request.
