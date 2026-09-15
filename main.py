"""Exemples des exercices 1 à 6."""

from lapin import Lapin


lapins = [
    Lapin(10, 10),
    Lapin(20, 30),
    Lapin(50, 20),
    Lapin(70, 40),
    Lapin(80, 80),
]

for lapin in lapins:
    lapin.vieillir()

print(f"Nombre de lapins : {len(lapins)}")
print(f"Âges après un tour : {[lapin.age for lapin in lapins]}")
