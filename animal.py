"""Classe Animal."""

import math
from abc import ABC, abstractmethod


class Animal(ABC):
    """Regrouper les caractéristiques communes aux animaux."""

    RAYON_DETECTION = 10
    COUT_DEPLACEMENT = 1
    COUT_REPRODUCTION = 30
    EST_PROIE = False
    EST_PREDATEUR = False

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self._energie = 100
        self.age = 0
        self.vitesse = 1

    @property
    def energie(self) -> int:
        """Lire l'énergie sans pouvoir la modifier directement."""
        return self._energie

    @abstractmethod
    def se_deplacer(self) -> None:
        """Déplacer l'animal selon son comportement propre."""
        ...

    @abstractmethod
    def reproduire(self) -> "Animal":
        """Créer un nouvel animal de la même espèce."""
        ...

    def agir(self, animaux: list) -> None:
        """Comportement par défaut d'un tour : se déplacer."""
        self.se_deplacer()

    def vieillir(self) -> None:
        """Augmenter l'âge de 1 et retirer 1 d'énergie."""
        self.age += 1
        self.perdre_energie(1)

    def perdre_energie(self, quantite: int) -> None:
        """Retirer de l'énergie sans descendre sous zéro."""
        self._energie = max(0, self._energie - quantite)

    def gagner_energie(self, quantite: int) -> None:
        """Ajouter de l'énergie."""
        self._energie += quantite

    def est_vivant(self) -> bool:
        """Indiquer si l'énergie est strictement positive."""
        return self._energie > 0

    def distance_avec(self, autre: "Animal") -> float:
        """Calculer la distance entre deux animaux."""
        return math.sqrt((autre.x - self.x) ** 2 + (autre.y - self.y) ** 2)

    def detecter(self, autre: "Animal") -> bool:
        """Indiquer si un autre animal est dans le rayon de détection."""
        return self.distance_avec(autre) <= self.RAYON_DETECTION

    def peut_se_reproduire(self) -> bool:
        """Indiquer si l'âge et l'énergie permettent la reproduction."""
        return self.age >= 5 and self.energie >= 60


if __name__ == "__main__":
    try:
        Animal(10, 10)
    except TypeError as erreur:
        print(erreur)
