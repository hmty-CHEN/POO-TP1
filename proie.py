"""Classe Proie."""

import random

from animal import Animal


class Proie(Animal):
    """Regrouper les comportements communs aux proies."""

    EST_PROIE = True
    GAIN_NOURRITURE = 20

    def se_deplacer(self) -> None:
        """Déplacer la proie d'une case le long d'un axe."""
        for _ in range(self.vitesse):
            if random.choice([True, False]):
                self.x += random.choice([-1, 1])
            else:
                self.y += random.choice([-1, 1])

    def fuir(self, menace: Animal) -> None:
        """Se déplacer d'une case sur l'axe qui éloigne le plus de la menace."""
        if not self.detecter(menace):
            return
        meilleur = None
        meilleure_distance = -1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            distance = (menace.x - (self.x + dx)) ** 2 + (menace.y - (self.y + dy)) ** 2
            if distance > meilleure_distance:
                meilleure_distance = distance
                meilleur = (dx, dy)
        self.x += meilleur[0]
        self.y += meilleur[1]

    def se_nourrir(self) -> None:
        """Gagner de l'énergie en se nourrissant."""
        self.gagner_energie(self.GAIN_NOURRITURE)

    def agir(self, animaux: list) -> None:
        """Fuir le prédateur détecté le plus proche, sinon se déplacer."""
        predateurs = [animal for animal in animaux if animal.EST_PREDATEUR and animal.est_vivant()]
        if predateurs:
            proche = min(predateurs, key=self.distance_avec)
            if self.detecter(proche):
                self.fuir(proche)
                return
        self.se_deplacer()
