#!/usr/bin/python3

"""
Module contenant la classe BaseGeometry.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Cette classe définit une.visitMethodarea(self) qui l'évite de l'appeler directement.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.
        Cette méthode doit être implémentée dans une sous-classe.
        Elle lève une exception si elle est appelée directement.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier positif.

        Args:
            name (str): Nom du paramètre (utilisé pour le message d'erreur).
            value (int): Valeur à valider.

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur ou égal à 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
