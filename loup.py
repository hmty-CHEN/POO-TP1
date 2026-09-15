"""Classe Loup."""

from lapin import Lapin
from predateur import Predateur


class Loup(Predateur):
    """Représenter un loup."""

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.vitesse = 2

    def reproduire(self) -> "Loup":
        """Créer un nouveau loup à la même position."""
        return Loup(self.x, self.y)


if __name__ == "__main__":
    loup = Loup(0, 0)
    lapin = Lapin(5, 0)
    animaux = [loup, lapin]

    for _ in range(6):
        loup.agir(animaux)
        print(loup.x, loup.y, lapin.x, lapin.y, lapin.est_vivant(), loup.energie)
