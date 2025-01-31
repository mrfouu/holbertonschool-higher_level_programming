#!/usr/bin/python3
"""
Définition d'une classe Rectangle avec des attributs width et height.
"""


class Rectangle:
    """
    Classe Rectangle,un rectangle avec une largeur et une hauteur.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Args:
            width (int): La largeur du rectangle (par défaut 0).
            height (int): La hauteur du rectangle (par défaut 0).

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est négatif.
        """
        self.width = width  # Utilisation du setter pour validation
        self.height = height  # Utilisation du setter pour validation

    @property
    def width(self):
        """Retourne la largeur actuelle du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle en s'assurant qu'elle est valide.

        Args:
            value (int): La nouvelle largeur du rectangle.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):  # Vérifie que la largeur est un entier
            raise TypeError("width must be an integer")
        if value < 0:  # Vérifie que la largeur est positive ou nulle
            raise ValueError("width must be >= 0")
        self.__width = value  # Stocke la valeur validée

    @property
    def height(self):
        """Retourne la hauteur actuelle du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle en s'assurant qu'elle est valide.

        Args:
            value (int): La nouvelle hauteur du rectangle.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):  # Vérifie que la hauteur est un entier
            raise TypeError("height must be an integer")
        if value < 0:  # Vérifie que la hauteur est positive ou nulle
            raise ValueError("height must be >= 0")
        self.__height = value  # Stocke la valeur validée

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height  # Aire = largeur × hauteur

    def perimeter(self):
        """Retourne le périmètre du rectangle.

        Si l'une des dimensions est 0, le périmètre est également 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
    # Périmètre = 2 × (largeur + hauteur)

    def __str__(self):
        """rectangle avec le caractère '#' sous forme de chaîne."""
        if self.__width == 0 or self.__height == 0:
            return ""  # Si une dimension est 0, on retourne une chaîne vide
        else:
            rectangle = []
            for i in range(self.__height):  # Boucle sur la hauteur
                rectangle.append("#" * self.__width)
                # Ajoute une ligne de '#' de longueur width
            return '\n'.join(rectangle)
        # Retourne le rectangle sous forme de chaîne
