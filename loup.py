"""Classe Loup."""

import random

from animal import Animal
from lapin import Lapin


class Loup(Animal):
    """Représenter un loup."""

    GAIN_CHASSE = 20

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.vitesse = 2

    def se_deplacer(self) -> None:
        """Déplacer le loup de deux cases le long des axes."""
        for _ in range(self.vitesse):
            if random.choice([True, False]):
                self.x += random.choice([-1, 1])
            else:
                self.y += random.choice([-1, 1])

    def rechercher_proies(self, animaux: list) -> list:
        """Renvoyer les lapins vivants détectés dans le rayon de détection."""
        return [
            animal
            for animal in animaux
            if isinstance(animal, Lapin) and animal.est_vivant() and self.detecter(animal)
        ]

    def se_deplacer_vers(self, cible: Animal) -> None:
        """Se déplacer vers la cible, une case par étape, en suivant les axes."""
        for _ in range(self.vitesse):
            dx = cible.x - self.x
            dy = cible.y - self.y
            if abs(dx) >= abs(dy) and dx != 0:
                self.x += 1 if dx > 0 else -1
            elif dy != 0:
                self.y += 1 if dy > 0 else -1

    def chasser(self, proie: Animal) -> None:
        """Attaquer une proie située à la même position."""
        if self.x == proie.x and self.y == proie.y:
            proie.perdre_energie(proie.energie)
            self.gagner_energie(self.GAIN_CHASSE)

    def reproduire(self) -> "Loup":
        """Créer un nouveau loup à la même position."""
        return Loup(self.x, self.y)


if __name__ == "__main__":
    loup = Loup(0, 0)
    lapin = Lapin(5, 0)
    animaux = [loup, lapin]

    for _ in range(6):
        proies = loup.rechercher_proies(animaux)
        if proies:
            loup.se_deplacer_vers(proies[0])
            loup.chasser(proies[0])
        print(loup.x, loup.y, lapin.x, lapin.y, lapin.est_vivant(), loup.energie)
