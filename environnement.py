"""Classe Environnement."""

from animal import Animal


class Environnement:
    """Représenter la grille et les animaux qu'elle contient."""

    def __init__(self, largeur: int, hauteur: int) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.animaux = []

    def ajouter(self, animal: Animal) -> None:
        """Ajouter un animal à l'environnement."""
        self.animaux.append(animal)

    def supprimer_morts(self) -> None:
        """Retirer les animaux qui ne sont plus vivants."""
        self.animaux = [animal for animal in self.animaux if animal.est_vivant()]

    def compter(self, espece: type) -> int:
        """Compter les animaux vivants d'une espèce."""
        return sum(isinstance(animal, espece) for animal in self.animaux)

    def simuler_un_tour(self) -> None:
        """Agir, consommer, vieillir, reproduire, puis retirer les morts."""
        for animal in list(self.animaux):
            animal.agir(self.animaux)
            animal.perdre_energie(Animal.COUT_DEPLACEMENT)
            animal.vieillir()

        nouveau = []
        for animal in list(self.animaux):
            if animal.est_vivant() and animal.peut_se_reproduire():
                animal.perdre_energie(Animal.COUT_REPRODUCTION)
                nouveau.append(animal.reproduire())
        self.animaux.extend(nouveau)

        self.supprimer_morts()

    def statistiques(self) -> dict:
        """Renvoyer les compteurs de population."""
        proies = sum(animal.EST_PROIE for animal in self.animaux)
        predateurs = sum(animal.EST_PREDATEUR for animal in self.animaux)
        return {"proies": proies, "predateurs": predateurs, "total": len(self.animaux)}


if __name__ == "__main__":
    from lapin import Lapin
    from loup import Loup

    environnement = Environnement(100, 100)
    environnement.ajouter(Lapin(10, 20))
    environnement.ajouter(Loup(80, 20))
    print(environnement.statistiques())
