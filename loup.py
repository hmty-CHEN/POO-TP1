"""Classe Loup."""

from animal import Animal


class Loup(Animal):
    """Représenter un loup."""

    def chasser(self) -> None:
        """Afficher le comportement de chasse."""
        print("Le loup chasse !")


if __name__ == "__main__":
    loup = Loup(80, 20)
    loup.vieillir()
    print(loup.x, loup.y, loup.age, loup.energie)
    loup.chasser()
