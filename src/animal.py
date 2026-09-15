"""Classe de base (abstraite) représentant un animal générique.

Cette classe regroupe les caractéristiques et les comportements communs à
tous les animaux : position, énergie, âge, vitesse, vieillissement,
gestion de l'énergie et survie.

Elle n'est pas destinée à être instanciée directement : les classes
`Proie` et `Predateur` (puis `Lapin` et `Loup`) la spécialisent.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal générique (classe abstraite)."""

    def __init__(
        self,
        x: int,
        y: int,
        energie: int = 100,
        age: int = 0,
        vitesse: int = 1,
    ) -> None:
        """Initialiser un animal.

        Args:
            x: position horizontale initiale.
            y: position verticale initiale.
            energie: énergie initiale (100 par défaut).
            age: âge initial (0 par défaut).
            vitesse: vitesse de déplacement (1 par défaut).
        """
        # TODO: définir les attributs de position, d'énergie, d'âge et de vitesse.
        raise NotImplementedError

    @abstractmethod
    def se_deplacer(self) -> None:
        """Déplacer l'animal selon son comportement propre.

        Chaque type d'animal fournit sa propre implémentation
        (polymorphisme).
        """
        raise NotImplementedError

    def vieillir(self) -> None:
        """Vieillir d'un an et perdre de l'énergie en conséquence."""
        # TODO: incrémenter l'âge et retirer l'énergie correspondante.
        raise NotImplementedError

    def perdre_energie(self, quantite: int) -> None:
        """Retirer de l'énergie tout en gardant un état cohérent."""
        # TODO: décrémenter l'énergie sans rendre l'objet incohérent.
        raise NotImplementedError

    def gagner_energie(self, quantite: int) -> None:
        """Ajouter de l'énergie (par exemple après une chasse)."""
        # TODO
        raise NotImplementedError

    def est_vivant(self) -> bool:
        """Indiquer si l'animal est encore vivant."""
        # TODO: retourner True tant que l'énergie est strictement positive.
        raise NotImplementedError

    def distance_avec(self, autre: "Animal") -> float:
        """Calculer la distance euclidienne entre deux animaux."""
        # TODO: utiliser math.sqrt et les coordonnées des deux animaux.
        raise NotImplementedError

    def peut_se_reproduire(self) -> bool:
        """Indiquer si les conditions de reproduction sont réunies."""
        # TODO: âge >= 5 et énergie >= 60 (règles du sujet).
        raise NotImplementedError

    @abstractmethod
    def reproduire(self) -> "Animal":
        """Créer un nouvel animal issu de la reproduction."""
        raise NotImplementedError
