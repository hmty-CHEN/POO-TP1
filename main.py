"""Démonstration du polymorphisme."""

from lapin import Lapin
from loup import Loup


animaux = [
    Lapin(10, 10),
    Loup(20, 20),
    Lapin(30, 30),
    Loup(40, 40),
]

for animal in animaux:
    animal.se_deplacer()
    print(type(animal).__name__, animal.x, animal.y)
