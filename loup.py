"""Classe Loup."""

import random

from animal import Animal


class Loup(Animal):
    """Représenter un loup."""

    def se_deplacer(self) -> None:
        """Déplacer le loup de deux cases dans une direction aléatoire."""
        self.x += 2 * random.choice([-1, 1])
        self.y += 2 * random.choice([-1, 1])

    def chasser(self) -> None:
        """Afficher le comportement de chasse."""
        print("Le loup chasse !")


if __name__ == "__main__":
    loup = Loup(80, 20)
    loup.se_deplacer()
    print(loup.x, loup.y)
    loup.chasser()
