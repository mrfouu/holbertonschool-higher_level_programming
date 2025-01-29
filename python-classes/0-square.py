#!/usr/bin/python3


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

        Arguments :
        size (int) : La taille du côté du carré (doit être un entier positif).
        """
        if not isinstance(size, int):  # Vérifie si size est un entier
            raise TypeError("size doit être un entier")
        if size < 0:  # Vérifie si size est positif ou nul
            raise ValueError("size doit être >= 0")
        self.__size = size  # Attribut privé pour stocker la taille du carré

    def area(self):
        """Retourne l'aire du carré (côté * côté)."""
        return self.__size ** 2
