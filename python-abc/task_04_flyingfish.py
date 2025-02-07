#!/usr/bin/env python3

class Fish:
    """
    Classe représentant un poisson.
    Elle contient des méthodes pour simuler le comportement d'un poisson.
    """
    def swim(self):
        """
        Méthode qui simule la nage du poisson.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Méthode qui décrit l'habitat du poisson.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.
    Elle contient des méthodes pour simuler le comportement d'un oiseau.
    """
    def fly(self):
        """
        Méthode qui simule le vol de l'oiseau.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Méthode qui décrit l'habitat de l'oiseau.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant qui hérite des comportements
    à la fois d'un poisson et d'un oiseau, mais avec des comportements spécifiques.
    """
    def __init__(self):
        """
        Méthode d'initialisation pour la classe FlyingFish.
        Elle permet d'initaliser les classes parentes si nécessaire.
        """
        super().__init__()

    def fly(self):
        """
        Redéfinition de la méthode 'fly' pour un poisson volant.
        Cette méthode remplace la méthode 'fly' de la classe Bird.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Redéfinition de la méthode 'swim' pour un poisson volant.
        Cette méthode remplace la méthode 'swim' de la classe Fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Redéfinition de la méthode 'habitat' pour le poisson volant.
        Cette méthode indique que le poisson volant vit à la fois dans l'eau et dans le ciel.
        """
        print("The flying fish lives both in water and the sky!")
        # Optionnellement, on peut appeler les méthodes 'habitat' des classes parentes :
        # Fish.habitat(self)  # Cela afficherait "The fish lives in water"
        # Bird.habitat(self)  # Cela afficherait "The bird lives in the sky"
