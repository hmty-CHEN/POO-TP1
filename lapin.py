"""Classe Lapin."""

import random

from animal import Animal


class Lapin(Animal):
    """Représenter un lapin."""

    def se_deplacer(self) -> None:
        """Déplacer le lapin d'une case dans une direction aléatoire."""
        self.x += random.choice([-1, 1])
        self.y += random.choice([-1, 1])

    def fuir(self, menace: Animal) -> None:
        """Se déplacer d'une case vers la position qui éloigne le plus de la menace."""
        meilleur_dx = 0
        meilleur_dy = 0
        meilleure_distance = -1
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                distance = (menace.x - (self.x + dx)) ** 2 + (menace.y - (self.y + dy)) ** 2
                if distance > meilleure_distance:
                    meilleure_distance = distance
                    meilleur_dx = dx
                    meilleur_dy = dy
        self.x += meilleur_dx
        self.y += meilleur_dy


if __name__ == "__main__":
    lapin = Lapin(0, 0)
    menace = Lapin(5, 0)
    lapin.fuir(menace)
    print(lapin.x, lapin.y)
