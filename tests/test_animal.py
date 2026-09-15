"""Tests unitaires liés aux animaux.

Les tests sont volontairement laissés à implémenter. Ils servent de
gabarit : chaque méthode doit être complétée puis activée en retirant
l'appel à `skipTest`.
"""

import unittest

from src.lapin import Lapin
from src.loup import Loup


class TestAnimal(unittest.TestCase):
    """Série de tests minimale exigée par le sujet."""

    def test_creation(self) -> None:
        """Un animal créé possède un âge de 0 et une énergie de 100."""
        self.skipTest("À implémenter")

    def test_vieillissement(self) -> None:
        """Après un tour, l'âge augmente et l'énergie diminue."""
        self.skipTest("À implémenter")

    def test_mort(self) -> None:
        """Un animal dont l'énergie atteint 0 est considéré comme mort."""
        self.skipTest("À implémenter")

    def test_deplacement(self) -> None:
        """Les coordonnées changent correctement après un déplacement."""
        self.skipTest("À implémenter")

    def test_chasse(self) -> None:
        """Un loup et un lapin à la même position : le lapin meurt et le
        loup gagne de l'énergie."""
        self.skipTest("À implémenter")


if __name__ == "__main__":
    unittest.main()
