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
├── main.py
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
| `main.py` | Point d'entrée : lance la simulation. |
| `rapport.html` | Rapport de cours en français. |
| `traduction-rapport.md` | Traduction chinoise du rapport. |

## Exécution

```bash
python main.py
```

## Organisation du travail

1. Créer une branche par fonctionnalité.
2. Faire des commits courts et explicites.
3. Pousser la branche puis ouvrir une pull request.
