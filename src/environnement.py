"""Classe représentant l'environnement (la grille) et les animaux.

L'environnement illustre la **composition** : il contient une collection
d'objets `Animal` et gère leur cycle de vie au fil des tours.
"""

from __future__ import annotations


class Environnement:
    """Grille contenant les animaux et gérant un tour de simulation."""

    def __init__(self, largeur: int, hauteur: int) -> None:
        """Créer un environnement de dimensions données.

        Args:
            largeur: nombre de colonnes de la grille.
            hauteur: nombre de lignes de la grille.
        """
        # TODO: stocker les dimensions et initialiser la liste des animaux.
        raise NotImplementedError

    def ajouter(self, animal) -> None:
        """Ajouter un animal à l'environnement."""
        # TODO
        raise NotImplementedError

    def supprimer_morts(self) -> None:
        """Retirer de l'environnement les animaux qui ne sont plus vivants."""
        # TODO: filtrer la collection d'animaux.
        raise NotImplementedError

    def animaux_vivants(self) -> list:
        """Renvoyer la liste des animaux encore vivants."""
        # TODO
        raise NotImplementedError

    def simuler_un_tour(self) -> None:
        """Exécuter un tour complet de simulation.

        Étapes attendues : déplacement, vieillissement, gestion de
        l'énergie, interactions, reproduction, puis suppression des morts.
        """
        # TODO
        raise NotImplementedError

    def statistiques(self) -> dict:
        """Renvoyer un dictionnaire de statistiques sur la population."""
        # TODO: par exemple nombre de proies, de prédateurs, total.
        raise NotImplementedError
