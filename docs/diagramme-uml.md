# Diagramme UML

> Diagramme de classes à compléter. Le bloc ci-dessous utilise la syntaxe
> Mermaid (rendu possible sur GitHub et dans de nombreux éditeurs).

```mermaid
classDiagram
    class Animal {
        <<abstract>>
        +int x
        +int y
        +int energie
        +int age
        +int vitesse
        +se_deplacer()*
        +vieillir()
        +perdre_energie(quantite)
        +gagner_energie(quantite)
        +est_vivant() bool
        +distance_avec(autre) float
        +peut_se_reproduire() bool
        +reproduire()* Animal
    }

    class Proie {
        <<abstract>>
        +se_deplacer()
        +fuir(menace)
        +se_nourrir()
        +reproduire() Animal
    }

    class Predateur {
        <<abstract>>
        +se_deplacer()
        +rechercher_proies(environnement) list
        +chasser(proie)
        +reproduire() Animal
    }

    class Lapin {
        +int VITESSE_PAR_DEFAUT
        +se_deplacer()
        +fuir(menace)
        +se_nourrir()
        +reproduire()
    }

    class Loup {
        +int VITESSE_PAR_DEFAUT
        +int RAYON_DETECTION
        +se_deplacer()
        +rechercher_proies(environnement)
        +chasser(proie)
        +reproduire()
    }

    class Environnement {
        +int largeur
        +int hauteur
        +list animaux
        +ajouter(animal)
        +supprimer_morts()
        +animaux_vivants() list
        +simuler_un_tour()
        +statistiques() dict
    }

    class Simulation {
        +Environnement environnement
        +int nombre_lapins
        +int nombre_loups
        +initialiser_populations()
        +executer(nombre_de_tours)
        +afficher_statistiques(tour)
    }

    Animal <|-- Proie
    Animal <|-- Predateur
    Proie <|-- Lapin
    Predateur <|-- Loup
    Environnement "1" *-- "0..*" Animal : contient
    Simulation "1" --> "1" Environnement : pilote
```

## À compléter

- [ ] Vérifier les attributs et méthodes définitifs.
- [ ] Confirmer les multiplicités des relations.
- [ ] Ajouter les contraintes éventuelles (rayon de détection, règles de
      reproduction).
- [ ] Préparer une version exportée en image pour le rendu.
