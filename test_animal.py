"""Tests unitaires des animaux."""

import unittest

from lapin import Lapin
from loup import Loup


class TestAnimal(unittest.TestCase):
    """Vérifier la création, le vieillissement, la mort, le déplacement et la chasse."""

    def test_creation(self) -> None:
        """Un animal créé possède un âge de 0 et une énergie de 100."""
        lapin = Lapin(10, 20)
        self.assertEqual(lapin.age, 0)
        self.assertEqual(lapin.energie, 100)

    def test_vieillissement(self) -> None:
        """Après un tour, l'âge augmente et l'énergie diminue."""
        lapin = Lapin(10, 20)
        age = lapin.age
        energie = lapin.energie
        lapin.vieillir()
        self.assertEqual(lapin.age, age + 1)
        self.assertEqual(lapin.energie, energie - 1)

    def test_mort(self) -> None:
        """Un animal dont l'énergie atteint 0 est mort."""
        lapin = Lapin(10, 20)
        lapin.perdre_energie(lapin.energie)
        self.assertEqual(lapin.energie, 0)
        self.assertFalse(lapin.est_vivant())

    def test_deplacement(self) -> None:
        """Le déplacement change les coordonnées d'une seule case."""
        lapin = Lapin(10, 20)
        position = (lapin.x, lapin.y)
        lapin.se_deplacer()
        self.assertNotEqual((lapin.x, lapin.y), position)
        self.assertEqual(abs(lapin.x - 10) + abs(lapin.y - 20), 1)

    def test_chasse(self) -> None:
        """Le lapin meurt et le loup gagne de l'énergie."""
        loup = Loup(10, 20)
        lapin = Lapin(10, 20)
        energie = loup.energie
        loup.chasser(lapin)
        self.assertFalse(lapin.est_vivant())
        self.assertGreater(loup.energie, energie)


if __name__ == "__main__":
    unittest.main()
