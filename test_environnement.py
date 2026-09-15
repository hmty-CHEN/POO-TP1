"""Tests unitaires de l'environnement."""

import unittest

from environnement import Environnement
from lapin import Lapin
from loup import Loup


class TestEnvironnement(unittest.TestCase):
    """Vérifier l'ajout, la suppression et les statistiques."""

    def test_ajout(self) -> None:
        """Le nombre d'animaux correspond au nombre d'ajouts."""
        environnement = Environnement(100, 100)
        environnement.ajouter(Lapin(10, 20))
        environnement.ajouter(Loup(80, 20))
        self.assertEqual(len(environnement.animaux), 2)

    def test_suppression_morts(self) -> None:
        """Un animal mort est retiré de l'environnement."""
        environnement = Environnement(100, 100)
        lapin = Lapin(10, 20)
        environnement.ajouter(lapin)
        lapin.perdre_energie(lapin.energie)
        environnement.supprimer_morts()
        self.assertEqual(len(environnement.animaux), 0)

    def test_statistiques(self) -> None:
        """Les statistiques comptent les proies et les prédateurs."""
        environnement = Environnement(100, 100)
        environnement.ajouter(Lapin(10, 20))
        environnement.ajouter(Lapin(30, 20))
        environnement.ajouter(Loup(80, 20))
        statistiques = environnement.statistiques()
        self.assertEqual(statistiques["proies"], 2)
        self.assertEqual(statistiques["predateurs"], 1)
        self.assertEqual(statistiques["total"], 3)

    def test_reproduction_en_couple(self) -> None:
        """Deux animaux proches de la même espèce produisent un petit."""
        environnement = Environnement(50, 50)
        premier = Lapin(10, 10)
        second = Lapin(12, 10)
        premier.age = second.age = 5
        environnement.ajouter(premier)
        environnement.ajouter(second)
        environnement.gerer_reproduction()
        self.assertEqual(len(environnement.animaux), 3)
        self.assertEqual(premier.energie, 70)
        self.assertEqual(second.energie, 70)

    def test_pas_de_reproduction_seul(self) -> None:
        """Un animal isolé ne peut pas se reproduire."""
        environnement = Environnement(50, 50)
        lapin = Lapin(10, 10)
        lapin.age = 5
        environnement.ajouter(lapin)
        environnement.gerer_reproduction()
        self.assertEqual(len(environnement.animaux), 1)


if __name__ == "__main__":
    unittest.main()
