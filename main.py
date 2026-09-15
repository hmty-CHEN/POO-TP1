"""Point d'entrée du programme."""

from simulation import Simulation


def main() -> None:
    """Lancer la simulation."""
    simulation = Simulation(nombre_lapins=10, nombre_loups=3)
    simulation.executer(nombre_de_tours=10)


if __name__ == "__main__":
    main()
