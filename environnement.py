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
        self.borner(animal)
        self.animaux.append(animal)

    def borner(self, animal: Animal) -> None:
        """Garder l'animal à l'intérieur de la grille."""
        animal.x = max(0, min(self.largeur - 1, animal.x))
        animal.y = max(0, min(self.hauteur - 1, animal.y))

    def supprimer_morts(self) -> None:
        """Retirer les animaux qui ne sont plus vivants."""
        self.animaux = [animal for animal in self.animaux if animal.est_vivant()]

    def retirer(self, animal: Animal) -> None:
        """Retirer un animal donné de l'environnement."""
        if animal in self.animaux:
            self.animaux.remove(animal)

    def compter(self, espece: type) -> int:
        """Compter les animaux vivants d'une espèce."""
        return sum(isinstance(animal, espece) for animal in self.animaux)

    def simuler_un_tour(self) -> None:
        """Agir, consommer, vieillir, reproduire, puis retirer les morts."""
        for animal in list(self.animaux):
            animal.agir(self.animaux)
            self.borner(animal)
            animal.perdre_energie(Animal.COUT_DEPLACEMENT)
            animal.vieillir()

        self.gerer_reproduction()
        self.supprimer_morts()

    def gerer_reproduction(self) -> None:
        """Former des couples proches de même espèce et créer les petits."""
        deja = []
        nouveau = []
        for animal in self.animaux:
            if animal in deja or not animal.peut_se_reproduire():
                continue
            partenaire = self._partenaire(animal, deja)
            if partenaire is None:
                continue
            animal.perdre_energie(Animal.COUT_REPRODUCTION)
            partenaire.perdre_energie(Animal.COUT_REPRODUCTION)
            deja.append(animal)
            deja.append(partenaire)
            nouveau.append(animal.reproduire())
        self.animaux.extend(nouveau)

    def _partenaire(self, animal: Animal, deja: list) -> Animal:
        """Chercher un partenaire proche, disponible et de la même espèce."""
        for autre in self.animaux:
            if autre is animal or autre in deja:
                continue
            if animal.peut_se_reproduire_avec(autre):
                return autre
        return None

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
