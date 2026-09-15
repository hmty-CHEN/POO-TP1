"""Démonstration de la chasse."""

from lapin import Lapin
from loup import Loup


loup = Loup(0, 0)
lapin = Lapin(5, 0)
animaux = [loup, lapin]

for tour in range(6):
    proies = loup.rechercher_proies(animaux)
    if proies:
        cible = proies[0]
        loup.se_deplacer_vers(cible)
        loup.chasser(cible)
    print(
        f"Tour {tour} : loup=({loup.x},{loup.y}) "
        f"lapin=({lapin.x},{lapin.y}) vivant={lapin.est_vivant()} "
        f"energie_loup={loup.energie}"
    )
