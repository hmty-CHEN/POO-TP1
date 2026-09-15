"""Classe gérant le déroulement global de la simulation.

La simulation crée l'environnement, initialise les populations, exécute
les tours et affiche les statistiques.
"""

from __future__ import annotations


class Simulation:
    """Orchestration d'une partie : populations, tours et statistiques."""

    def __init__(
        self,
        largeur: int = 100,
        hauteur: int = 100,
        nombre_lapins: int = 10,
        nombre_loups: int = 3,
    ) -> None:
        """Configurer la simulation.

        Args:
            largeur: largeur de l'environnement.
            hauteur: hauteur de l'environnement.
            nombre_lapins: nombre initial de lapins.
            nombre_loups: nombre initial de loups.
        """
        # TODO: créer l'environnement et retenir les paramètres.
        raise NotImplementedError

    def initialiser_populations(self) -> None:
        """Placer les animaux de départ aléatoirement dans l'environnement."""
        # TODO
        raise NotImplementedError

    def executer(self, nombre_de_tours: int = 50) -> None:
        """Exécuter la simulation sur un nombre de tours donné."""
        # TODO: boucle principale appelant `simuler_un_tour` et l'affichage.
        raise NotImplementedError

    def afficher_statistiques(self, tour: int) -> None:
        """Afficher les statistiques du tour courant.

        Exemple de rendu attendu :
            Tour : 25
            Proies : 73
            Prédateurs : 12
            Total : 85
        """
        # TODO
        raise NotImplementedError
