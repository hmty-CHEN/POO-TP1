"""Classe Lapin."""

import random

from animal import Animal


class Lapin(Animal):
    """Représenter un lapin."""

    RAYON_DETECTION = 4

    def se_deplacer(self) -> None:
        """Déplacer le lapin d'une case le long d'un axe."""
        for _ in range(self.vitesse):
            if random.choice([True, False]):
                self.x += random.choice([-1, 1])
            else:
                self.y += random.choice([-1, 1])

    def fuir(self, menace: Animal) -> None:
        """Se déplacer d'une case sur l'axe qui éloigne le plus de la menace détectée."""
        if not self.detecter(menace):
            return
        meilleur = None
        meilleure_distance = -1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            distance = (menace.x - (self.x + dx)) ** 2 + (menace.y - (self.y + dy)) ** 2
            if distance > meilleure_distance:
                meilleure_distance = distance
                meilleur = (dx, dy)
        self.x += meilleur[0]
        self.y += meilleur[1]

    def reproduire(self) -> "Lapin":
        """Créer un nouveau lapin à la même position."""
        return Lapin(self.x, self.y)


if __name__ == "__main__":
    from loup import Loup

    lapin = Lapin(0, 0)
    loup = Loup(3, 0)
    print(lapin.detecter(loup))
    lapin.fuir(loup)
    print(lapin.x, lapin.y)
