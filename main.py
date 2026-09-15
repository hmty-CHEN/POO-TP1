"""Démonstration de l'environnement."""

from environnement import Environnement
from lapin import Lapin
from loup import Loup


environnement = Environnement(100, 100)
for _ in range(5):
    environnement.ajouter(Lapin(50, 50))
environnement.ajouter(Loup(60, 60))

for tour in range(12):
    environnement.simuler_un_tour()
    print(
        f"Tour {tour} : proies={environnement.compter(Lapin)} "
        f"predateurs={environnement.compter(Loup)} "
        f"total={len(environnement.animaux)}"
    )
