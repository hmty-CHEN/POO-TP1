"""Classe Lapin."""

from proie import Proie


class Lapin(Proie):
    """Représenter un lapin."""

    RAYON_DETECTION = 4

    def reproduire(self) -> "Lapin":
        """Créer un nouveau lapin à la même position."""
        return Lapin(self.x, self.y)
