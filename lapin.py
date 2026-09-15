"""Première version simple de la classe Lapin.

Cette version couvre uniquement les exercices 1 à 6 du TP.
"""

import unittest


class Lapin:
    """Représenter un lapin dans l'écosystème."""

    def __init__(self, x: int, y: int) -> None:
        """Créer un lapin avec ses valeurs initiales."""
        self.x = x
        self.y = y
        self.energie = 100
        self.age = 0
        self.vitesse = 1

    def se_deplacer(self, dx: int, dy: int) -> None:
        """Modifier la position du lapin."""
        self.x += dx
        self.y += dy

    def vieillir(self) -> None:
        """Faire vieillir le lapin d'un an et réduire son énergie."""
        self.age += 1
        self.energie -= 1

    def est_vivant(self) -> bool:
        """Retourner True si l'énergie est strictement positive."""
        return self.energie > 0


class TestLapin(unittest.TestCase):
    """Tests simples conservés dans le même fichier que la classe."""

    def test_creation(self) -> None:
        lapin = Lapin(10, 20)
        self.assertEqual((lapin.x, lapin.y), (10, 20))
        self.assertEqual(lapin.energie, 100)
        self.assertEqual(lapin.age, 0)
        self.assertEqual(lapin.vitesse, 1)

    def test_deplacement(self) -> None:
        lapin = Lapin(10, 20)
        lapin.se_deplacer(3, -2)
        self.assertEqual((lapin.x, lapin.y), (13, 18))

    def test_vieillissement(self) -> None:
        lapin = Lapin(10, 20)
        lapin.vieillir()
        self.assertEqual(lapin.age, 1)
        self.assertEqual(lapin.energie, 99)

    def test_mort(self) -> None:
        lapin = Lapin(10, 20)
        lapin.energie = 0
        self.assertFalse(lapin.est_vivant())


if __name__ == "__main__":
    unittest.main()
