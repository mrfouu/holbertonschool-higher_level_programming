#!/usr/bin/python3
"""Définit une classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré (doit être un entier >= 0).
        """
        self.size = size  # Utilisation du setter pour gérer les validations

    @property
    def size(self):
        """Récupère la taille actuelle du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré en s'assurant qu'elle est valide.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):  # Vérifie que value est un entier
            raise TypeError("size must be an integer")
        elif value < 0:  # Vérifie que value est positif ou nul
            raise ValueError("size must be >= 0")
        self.__size = value  # Stocke la valeur validée dans l'attribut privé

    def area(self):
        """Retourne l'aire actuelle du carré."""
        return self.__size * self.__size  # Calcul de l'aire (côté * côté)
