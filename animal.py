"""Classe Animal."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Regrouper les caractéristiques communes aux animaux."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.energie = 100
        self.age = 0
        self.vitesse = 1

    @abstractmethod
    def se_deplacer(self) -> None:
        """Déplacer l'animal selon son comportement propre."""
        ...

    def vieillir(self) -> None:
        """Augmenter l'âge de 1 et retirer 1 d'énergie."""
        self.age += 1
        self.energie -= 1

    def est_vivant(self) -> bool:
        """Indiquer si l'énergie est strictement positive."""
        return self.energie > 0


if __name__ == "__main__":
    try:
        Animal(10, 10)
    except TypeError as erreur:
        print(erreur)
