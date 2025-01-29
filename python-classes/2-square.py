#!/usr/bin/python3
"""Définit une classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré (doit être un entier >= 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):  # Vérifie que size est bien un entier
            raise TypeError("size must be an integer")
        elif size < 0:  # Vérifie que size est positif ou nul
            raise ValueError("size must be >= 0")

        self.__size = size  # Stocke la taille du carré dans un attribut privé
