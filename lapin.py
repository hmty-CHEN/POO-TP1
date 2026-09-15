"""Classe Lapin."""

from animal import Animal


class Lapin(Animal):
    """Représenter un lapin."""

    def fuir(self) -> None:
        """Afficher le comportement de fuite."""
        print("Le lapin fuit !")


if __name__ == "__main__":
    lapin = Lapin(10, 20)
    lapin.vieillir()
    print(lapin.x, lapin.y, lapin.age, lapin.energie)
    lapin.fuir()
