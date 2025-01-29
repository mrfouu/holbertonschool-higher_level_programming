#!/usr/bin/python3
"""Définit une classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):  # Vérifie que size est un entier
            raise TypeError("size doit être un entier")
        if size < 0:  # Vérifie que size est positif ou nul
            raise ValueError("size doit être >= 0")

        self.__size = size  # Stocke la taille du carré dans un attribut privé
