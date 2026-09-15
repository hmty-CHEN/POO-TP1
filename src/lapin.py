"""Classe concrète du lapin (proie).

Le lapin est une proie simple : il se déplace d'une case et fuit les
prédateurs proches.
"""

from __future__ import annotations

from .proie import Proie


class Lapin(Proie):
    """Lapin : proie de référence du sujet."""

    VITESSE_PAR_DEFAUT = 1

    def __init__(self, x: int, y: int) -> None:
        """Créer un lapin aux coordonnées données.

        Args:
            x: position horizontale initiale.
            y: position verticale initiale.
        """
        # TODO: appeler le constructeur de Proie / Animal avec les valeurs
        # par défaut du sujet (énergie 100, âge 0, vitesse 1).
        raise NotImplementedError

    def se_deplacer(self) -> None:
        """Déplacer le lapin d'une case."""
        # TODO: choisir une direction et mettre à jour la position.
        raise NotImplementedError

    def fuir(self, menace=None) -> None:
        """Fuir une menace (afficher un message dans un premier temps)."""
        # TODO
        raise NotImplementedError

    def se_nourrir(self) -> None:
        """Manger une ressource et récupérer de l'énergie."""
        # TODO
        raise NotImplementedError

    def reproduire(self):
        """Créer un nouveau lapin."""
        # TODO
        raise NotImplementedError
