"""Classe Simulation."""

import random

from environnement import Environnement
from lapin import Lapin
from loup import Loup


class Simulation:
    """Créer l'environnement, les populations et dérouler les tours."""

    def __init__(
        self,
        largeur: int = 100,
        hauteur: int = 100,
        nombre_lapins: int = 10,
        nombre_loups: int = 3,
    ) -> None:
        self.environnement = Environnement(largeur, hauteur)
        self.nombre_lapins = nombre_lapins
        self.nombre_loups = nombre_loups

    def initialiser_populations(self) -> None:
        """Placer aléatoirement les lapins et les loups de départ."""
        largeur = self.environnement.largeur
        hauteur = self.environnement.hauteur
        for _ in range(self.nombre_lapins):
            self.environnement.ajouter(Lapin(random.randint(0, largeur), random.randint(0, hauteur)))
        for _ in range(self.nombre_loups):
            self.environnement.ajouter(Loup(random.randint(0, largeur), random.randint(0, hauteur)))

    def executer(self, nombre_de_tours: int = 10) -> None:
        """Exécuter la simulation sur un nombre de tours donné."""
        self.initialiser_populations()
        for tour in range(1, nombre_de_tours + 1):
            self.environnement.simuler_un_tour()
            self.afficher_statistiques(tour)

    def afficher_statistiques(self, tour: int) -> None:
        """Afficher les statistiques du tour courant."""
        statistiques = self.environnement.statistiques()
        print(f"Tour : {tour}")
        print(f"Proies : {statistiques['proies']}")
        print(f"Prédateurs : {statistiques['predateurs']}")
        print(f"Total : {statistiques['total']}")
