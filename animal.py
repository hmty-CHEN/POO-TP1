"""Classe Animal."""


class Animal:
    """Regrouper les caractéristiques communes aux animaux."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.energie = 100
        self.age = 0
        self.vitesse = 1

    def se_deplacer(self, dx: int, dy: int) -> None:
        """Ajouter le déplacement aux coordonnées."""
        self.x += dx
        self.y += dy

    def vieillir(self) -> None:
        """Augmenter l'âge de 1 et retirer 1 d'énergie."""
        self.age += 1
        self.energie -= 1

    def est_vivant(self) -> bool:
        """Indiquer si l'énergie est strictement positive."""
        return self.energie > 0
