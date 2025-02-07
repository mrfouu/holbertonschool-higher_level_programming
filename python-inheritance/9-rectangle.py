#!/usr/bin/python3
"""
Module définissant la classe Rectangle héritant de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle en validant ses dimensions.

        Args:
            width (int): La largeur du rectangle (doit être un entier positif).
            height (int): La hauteur du rectangle (doit être un entier positif).

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est inférieur ou égal à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Représente une chaîne de caractères pour le rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
