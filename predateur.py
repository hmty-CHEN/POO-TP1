"""Classe Predateur."""

import random

from animal import Animal


class Predateur(Animal):
    """Regrouper les comportements communs aux prédateurs."""

    EST_PREDATEUR = True
    GAIN_CHASSE = 20

    def se_deplacer(self) -> None:
        """Déplacer le prédateur de deux cases le long des axes."""
        for _ in range(self.vitesse):
            if random.choice([True, False]):
                self.x += random.choice([-1, 1])
            else:
                self.y += random.choice([-1, 1])

    def rechercher_proies(self, animaux: list) -> list:
        """Renvoyer les proies vivantes détectées dans le rayon de détection."""
        return [
            animal
            for animal in animaux
            if animal.EST_PROIE and animal.est_vivant() and self.detecter(animal)
        ]

    def se_deplacer_vers(self, cible: Animal) -> None:
        """Se déplacer vers la cible, une case par étape, en suivant les axes."""
        for _ in range(self.vitesse):
            dx = cible.x - self.x
            dy = cible.y - self.y
            if abs(dx) >= abs(dy) and dx != 0:
                self.x += 1 if dx > 0 else -1
            elif dy != 0:
                self.y += 1 if dy > 0 else -1

    def chasser(self, proie: Animal) -> None:
        """Attaquer une proie située à la même position."""
        if self.x == proie.x and self.y == proie.y:
            proie.perdre_energie(proie.energie)
            self.gagner_energie(self.GAIN_CHASSE)

    def agir(self, animaux: list) -> None:
        """Poursuivre et attaquer une proie détectée, sinon se déplacer."""
        proies = self.rechercher_proies(animaux)
        if proies:
            cible = min(proies, key=self.distance_avec)
            self.se_deplacer_vers(cible)
            self.chasser(cible)
            return
        self.se_deplacer()
