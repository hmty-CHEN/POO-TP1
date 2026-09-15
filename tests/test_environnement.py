"""Tests unitaires liés à l'environnement.

Comme pour les tests d'animaux, ces tests sont des gabarits à compléter.
"""

import unittest

from src.environnement import Environnement
from src.lapin import Lapin


class TestEnvironnement(unittest.TestCase):
    """Tests de la composition et de la gestion des populations."""

    def test_ajout_animaux(self) -> None:
        """Le nombre d'animaux correspond au nombre d'ajouts."""
        self.skipTest("À implémenter")

    def test_suppression_morts(self) -> None:
        """Un animal mort est retiré de l'environnement."""
        self.skipTest("À implémenter")


if __name__ == "__main__":
    unittest.main()
