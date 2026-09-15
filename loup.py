"""Classe Loup."""

import random

from animal import Animal
from lapin import Lapin


class Loup(Animal):
    """Représenter un loup."""

    RAYON_DETECTION = 10
    GAIN_CHASSE = 20

    def se_deplacer(self) -> None:
        """Déplacer le loup de deux cases dans une direction aléatoire."""
        self.x += 2 * random.choice([-1, 1])
        self.y += 2 * random.choice([-1, 1])

    def rechercher_proies(self, animaux: list) -> list:
        """Renvoyer les lapins vivants détectés dans le rayon de détection."""
        return [
            animal
            for animal in animaux
            if isinstance(animal, Lapin)
            and animal.est_vivant()
            and self.distance_avec(animal) <= self.RAYON_DETECTION
        ]

    def se_deplacer_vers(self, cible: Animal) -> None:
        """Se déplacer de deux cases vers une cible."""
        for _ in range(2):
            if self.x < cible.x:
                self.x += 1
            elif self.x > cible.x:
                self.x -= 1
            elif self.y < cible.y:
                self.y += 1
            elif self.y > cible.y:
                self.y -= 1

    def chasser(self, proie: Animal) -> None:
        """Attaquer une proie située à la même position."""
        if self.x == proie.x and self.y == proie.y:
            proie.perdre_energie(proie.energie)
            self.gagner_energie(self.GAIN_CHASSE)


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
