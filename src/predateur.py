"""Classe abstraite des prédateurs (par exemple les loups).

Un prédateur hérite d'`Animal` et ajoute la recherche de proies et la
chasse.
"""

from __future__ import annotations

from .animal import Animal


class Predateur(Animal):
    """Animal carnivore pouvant rechercher et chasser des proies."""

    def se_deplacer(self) -> None:
        """Se déplacer selon le comportement d'un prédateur."""
        # TODO
        raise NotImplementedError

    def rechercher_proies(self, environnement: "object") -> list[Animal]:
        """Renvoyer les proies situées dans le rayon de détection."""
        # TODO
        raise NotImplementedError

    def chasser(self, proie: Animal) -> None:
        """Attaquer une proie située à la même position."""
        # TODO
        raise NotImplementedError

    def reproduire(self) -> Animal:
        """Créer un nouveau prédateur."""
        # TODO
        raise NotImplementedError
