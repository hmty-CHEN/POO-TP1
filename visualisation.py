"""Visualisation graphique de la simulation avec tkinter."""

import random
import tkinter as tk
from tkinter import ttk

from environnement import Environnement
from lapin import Lapin
from loup import Loup


TAILLE_CASE = 8
LARGEUR_DEFAUT = 60
HAUTEUR_DEFAUT = 40
VITESSE_MS = 200
COULEUR_LAPIN = "#43a047"
COULEUR_LOUP = "#e53935"


class Application(tk.Tk):
    """Fenêtre principale : grille, paramètres, actions et statistiques."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Simulation d'un écosystème proie-prédateur")
        self.minsize(760, 520)

        self.environnement = Environnement(LARGEUR_DEFAUT, HAUTEUR_DEFAUT)
        self.tour_courant = 0
        self.en_cours = False

        self._construire_interface()
        self._initialiser()

    def _construire_interface(self) -> None:
        """Construire les cadres de la fenêtre."""
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        cadre_grille = ttk.LabelFrame(self, text="Écosystème", padding=8)
        cadre_grille.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.canevas = tk.Canvas(
            cadre_grille,
            width=self.environnement.largeur * TAILLE_CASE,
            height=self.environnement.hauteur * TAILLE_CASE,
            background="white",
            highlightthickness=1,
            highlightbackground="#bdbdbd",
        )
        self.canevas.pack()

        panneau = ttk.Frame(self)
        panneau.grid(row=0, column=1, sticky="n", padx=(0, 10), pady=10)

        cadre_parametres = ttk.LabelFrame(panneau, text="Paramètres", padding=8)
        cadre_parametres.pack(fill="x")
        self.champ_largeur = self._champ(cadre_parametres, "Largeur", LARGEUR_DEFAUT)
        self.champ_hauteur = self._champ(cadre_parametres, "Hauteur", HAUTEUR_DEFAUT)
        self.champ_lapins = self._champ(cadre_parametres, "Lapins", 20)
        self.champ_loups = self._champ(cadre_parametres, "Loups", 5)
        self.champ_vitesse = self._champ(cadre_parametres, "Intervalle (ms)", VITESSE_MS)
        ttk.Button(
            cadre_parametres, text="Initialiser", command=self._initialiser
        ).pack(fill="x", pady=(8, 0))

        cadre_actions = ttk.LabelFrame(panneau, text="Actions", padding=8)
        cadre_actions.pack(fill="x", pady=(10, 0))
        self.bouton_play = ttk.Button(cadre_actions, text="Démarrer", command=self._basculer)
        self.bouton_play.pack(fill="x", pady=2)
        ttk.Button(cadre_actions, text="Un tour", command=self._un_tour).pack(fill="x", pady=2)
        ttk.Button(
            cadre_actions, text="Ajouter un lapin", command=self._ajouter_lapin
        ).pack(fill="x", pady=2)
        ttk.Button(
            cadre_actions, text="Ajouter un loup", command=self._ajouter_loup
        ).pack(fill="x", pady=2)
        ttk.Button(
            cadre_actions, text="Supprimer les morts", command=self._supprimer_morts
        ).pack(fill="x", pady=2)

        cadre_statistiques = ttk.LabelFrame(panneau, text="Statistiques", padding=8)
        cadre_statistiques.pack(fill="x", pady=(10, 0))
        self.etiquettes = {}
        for cle, texte in (
            ("tour", "Tour"),
            ("proies", "Proies"),
            ("predateurs", "Prédateurs"),
            ("total", "Total"),
        ):
            ligne = ttk.Frame(cadre_statistiques)
            ligne.pack(fill="x")
            ttk.Label(ligne, text=f"{texte} :", width=12).pack(side="left")
            valeur = ttk.Label(ligne, text="0")
            valeur.pack(side="left")
            self.etiquettes[cle] = valeur

        cadre_legende = ttk.LabelFrame(panneau, text="Légende", padding=8)
        cadre_legende.pack(fill="x", pady=(10, 0))
        self._legende(cadre_legende, COULEUR_LAPIN, "Lapin (proie)")
        self._legende(cadre_legende, COULEUR_LOUP, "Loup (prédateur)")

    def _champ(self, parent: ttk.Frame, texte: str, valeur: int) -> ttk.Entry:
        """Créer un champ de saisie étiqueté."""
        ligne = ttk.Frame(parent)
        ligne.pack(fill="x", pady=2)
        ttk.Label(ligne, text=texte, width=14).pack(side="left")
        entree = ttk.Entry(ligne, width=8)
        entree.insert(0, str(valeur))
        entree.pack(side="left")
        return entree

    @staticmethod
    def _legende(parent: ttk.Frame, couleur: str, texte: str) -> None:
        """Afficher une pastille de couleur suivie de son libellé."""
        ligne = ttk.Frame(parent)
        ligne.pack(fill="x", pady=1)
        pastille = tk.Canvas(ligne, width=12, height=12, highlightthickness=0)
        pastille.create_oval(1, 1, 11, 11, fill=couleur, outline="")
        pastille.pack(side="left")
        ttk.Label(ligne, text=texte).pack(side="left", padx=(6, 0))

    @staticmethod
    def _lire(entree: ttk.Entry, defaut: int, minimum: int, maximum: int) -> int:
        """Lire un entier dans un champ, avec une valeur par défaut et des bornes."""
        try:
            return max(minimum, min(maximum, int(entree.get())))
        except ValueError:
            return defaut

    def _initialiser(self) -> None:
        """Relire les paramètres et recréer l'environnement."""
        self.en_cours = False
        self.bouton_play.config(text="Démarrer")
        largeur = self._lire(self.champ_largeur, LARGEUR_DEFAUT, 10, 120)
        hauteur = self._lire(self.champ_hauteur, HAUTEUR_DEFAUT, 10, 120)
        nombre_lapins = self._lire(self.champ_lapins, 20, 0, 500)
        nombre_loups = self._lire(self.champ_loups, 5, 0, 200)

        self.environnement = Environnement(largeur, hauteur)
        for _ in range(nombre_lapins):
            self.environnement.ajouter(Lapin(random.randrange(largeur), random.randrange(hauteur)))
        for _ in range(nombre_loups):
            self.environnement.ajouter(Loup(random.randrange(largeur), random.randrange(hauteur)))

        self.tour_courant = 0
        self.canevas.config(width=largeur * TAILLE_CASE, height=hauteur * TAILLE_CASE)
        self._dessiner()
        self._mettre_a_jour_statistiques()

    def _basculer(self) -> None:
        """Démarrer ou mettre en pause la simulation."""
        if self.en_cours:
            self.en_cours = False
            self.bouton_play.config(text="Démarrer")
        else:
            self.en_cours = True
            self.bouton_play.config(text="Pause")
            self._boucle()

    def _boucle(self) -> None:
        """Exécuter un tour puis se replanifier tant que la simulation tourne."""
        if not self.en_cours:
            return
        self._un_tour()
        intervalle = self._lire(self.champ_vitesse, VITESSE_MS, 20, 2000)
        self.after(intervalle, self._boucle)

    def _un_tour(self) -> None:
        """Avancer d'un tour et rafraîchir l'affichage."""
        self.environnement.simuler_un_tour()
        self.tour_courant += 1
        self._dessiner()
        self._mettre_a_jour_statistiques()

    def _ajouter_lapin(self) -> None:
        """Ajouter un lapin à une position aléatoire."""
        largeur = self.environnement.largeur
        hauteur = self.environnement.hauteur
        self.environnement.ajouter(Lapin(random.randrange(largeur), random.randrange(hauteur)))
        self._dessiner()
        self._mettre_a_jour_statistiques()

    def _ajouter_loup(self) -> None:
        """Ajouter un loup à une position aléatoire."""
        largeur = self.environnement.largeur
        hauteur = self.environnement.hauteur
        self.environnement.ajouter(Loup(random.randrange(largeur), random.randrange(hauteur)))
        self._dessiner()
        self._mettre_a_jour_statistiques()

    def _supprimer_morts(self) -> None:
        """Retirer de la grille les animaux qui ne sont plus vivants."""
        self.environnement.supprimer_morts()
        self._dessiner()
        self._mettre_a_jour_statistiques()

    def _dessiner(self) -> None:
        """Redessiner tous les animaux sur la grille."""
        self.canevas.delete("animal")
        for animal in self.environnement.animaux:
            couleur = COULEUR_LOUP if animal.EST_PREDATEUR else COULEUR_LAPIN
            x = animal.x * TAILLE_CASE
            y = animal.y * TAILLE_CASE
            self.canevas.create_oval(
                x, y, x + TAILLE_CASE, y + TAILLE_CASE, fill=couleur, outline="", tags="animal"
            )

    def _mettre_a_jour_statistiques(self) -> None:
        """Afficher le tour courant et les compteurs de population."""
        statistiques = self.environnement.statistiques()
        self.etiquettes["tour"].config(text=str(self.tour_courant))
        self.etiquettes["proies"].config(text=str(statistiques["proies"]))
        self.etiquettes["predateurs"].config(text=str(statistiques["predateurs"]))
        self.etiquettes["total"].config(text=str(statistiques["total"]))


def main() -> None:
    """Ouvrir la fenêtre de visualisation."""
    Application().mainloop()


if __name__ == "__main__":
    main()
