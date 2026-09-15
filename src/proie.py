"""Classe abstraite des proies (par exemple les lapins).

Une proie hérite d'`Animal` et ajoute des comportements propres aux
animaux qui se nourrissent et qui fuient face à un prédateur.
"""

from __future__ import annotations

from .animal import Animal


class Proie(Animal):
    """Animal herbivore pouvant se nourrir et fuir."""

    def se_deplacer(self) -> None:
        """Se déplacer selon le comportement d'une proie."""
        # TODO
        raise NotImplementedError

    def fuir(self, menace: Animal | None = None) -> None:
        """S'éloigner d'une menace détectée."""
        # TODO
        raise NotImplementedError

    def se_nourrir(self) -> None:
        """Se nourrir et récupérer de l'énergie."""
        # TODO
        raise NotImplementedError

    def reproduire(self) -> Animal:
        """Créer une nouvelle proie."""
        # TODO
        raise NotImplementedError
