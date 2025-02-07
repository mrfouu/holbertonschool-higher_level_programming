#!/usr/bin/python3

"""
Module contenant la classe BaseGeometry.

Cette classe sert de base pour définir des formes géométriques.
Elle contient une méthode `area` qui doit être implémentée par
les classes dérivées.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Cette classe définit une méthode `area` qui lève une exception
    car elle doit être implémentée dans les sous-classes.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Cette méthode doit être implémentée dans une sous-classe.
        Elle lève une exception si elle est appelée directement.
        """
        raise Exception("area() is not implemented")
