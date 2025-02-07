#!/usr/bin/python3
"""
Module définissant la classe Rectangle héritant de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle en validant ses dimensions.

        Args:
            width (int): Largeur du rectangle (doit être un entier positif).
            height (int): Hauteur du rectangle (doit être un entier positif).

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
