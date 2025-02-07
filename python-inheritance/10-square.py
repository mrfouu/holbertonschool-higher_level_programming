#!/usr/bin/python3
"""
Module définissant la classe Square héritant de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré.
    """

    def __init__(self, size):
        """
        Initialise un carré en validant sa taille.

        Args:
            size (int): La taille du côté du carré (doit être un entier positif).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Représente une chaîne de caractères pour le carré.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
