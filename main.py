"""Démonstration de la fuite et de la chasse."""

from lapin import Lapin
from loup import Loup


loup = Loup(0, 0)
lapin = Lapin(8, 0)
animaux = [loup, lapin]

for tour in range(20):
    if lapin.est_vivant():
        if lapin.detecter(loup):
            lapin.fuir(loup)
        else:
            lapin.se_deplacer()
    proies = loup.rechercher_proies(animaux)
    if proies:
        loup.se_deplacer_vers(proies[0])
        loup.chasser(proies[0])
    print(
        f"Tour {tour} : loup=({loup.x},{loup.y}) "
        f"lapin=({lapin.x},{lapin.y}) vivant={lapin.est_vivant()} "
        f"energie_loup={loup.energie}"
    )
