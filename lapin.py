"""Classe Lapin."""

import random

from animal import Animal


class Lapin(Animal):
    """Représenter un lapin."""

    def se_deplacer(self) -> None:
        """Déplacer le lapin d'une case dans une direction aléatoire."""
        self.x += random.choice([-1, 1])
        self.y += random.choice([-1, 1])

    def fuir(self) -> None:
        """Afficher le comportement de fuite."""
        print("Le lapin fuit !")


if __name__ == "__main__":
    lapin = Lapin(10, 20)
    lapin.se_deplacer()
    print(lapin.x, lapin.y)
    lapin.fuir()
