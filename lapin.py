"""Classe Lapin."""

import random

from animal import Animal


class Lapin(Animal):
    """Représenter un lapin."""

    def se_deplacer(self) -> None:
        """Déplacer le lapin d'une case le long d'un axe."""
        for _ in range(self.vitesse):
            if random.choice([True, False]):
                self.x += random.choice([-1, 1])
            else:
                self.y += random.choice([-1, 1])

    def fuir(self) -> None:
        """Afficher le comportement de fuite."""
        print("Le lapin fuit !")


if __name__ == "__main__":
    lapin = Lapin(10, 20)
    lapin.se_deplacer()
    lapin.vieillir()
    print(lapin.x, lapin.y, lapin.age, lapin.energie)
    lapin.fuir()
