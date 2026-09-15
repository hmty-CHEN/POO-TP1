"""Classe concrète du loup (prédateur).

Le loup est un prédateur : il se déplace de deux cases, détecte les
proies dans un rayon donné et les chasse.
"""

from __future__ import annotations

from .predateur import Predateur


class Loup(Predateur):
    """Loup : prédateur de référence du sujet."""

    VITESSE_PAR_DEFAUT = 2
    RAYON_DETECTION = 10

    def __init__(self, x: int, y: int) -> None:
        """Créer un loup aux coordonnées données.

        Args:
            x: position horizontale initiale.
            y: position verticale initiale.
        """
        # TODO: appeler le constructeur de Predateur / Animal avec les
        # valeurs par défaut du sujet (énergie 100, âge 0, vitesse 2).
        raise NotImplementedError

    def se_deplacer(self) -> None:
        """Déplacer le loup de deux cases."""
        # TODO
        raise NotImplementedError

    def rechercher_proies(self, environnement):
        """Renvoyer les proies détectées dans le rayon de détection."""
        # TODO
        raise NotImplementedError

    def chasser(self, proie) -> None:
        """Chasser une proie située à la même position."""
        # TODO: si les positions coïncident, la proie meurt et le loup
        # gagne de l'énergie.
        raise NotImplementedError

    def reproduire(self):
        """Créer un nouveau loup."""
        # TODO
        raise NotImplementedError
