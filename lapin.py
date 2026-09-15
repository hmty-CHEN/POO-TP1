"""Classe Lapin."""


class Lapin:
    """Représenter un lapin."""

    def __init__(self, x: int, y: int) -> None:
        """Initialiser la position, l'énergie, l'âge et la vitesse."""
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


if __name__ == "__main__":
    lapin = Lapin(10, 20)
    print(lapin.x, lapin.y)
    print(lapin.energie, lapin.age, lapin.vitesse)

    lapin.se_deplacer(3, -2)
    print(lapin.x, lapin.y)

    lapin.vieillir()
    print(lapin.age, lapin.energie)

    lapin.energie = 0
    print(lapin.est_vivant())
