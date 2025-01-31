#!/usr/bin/python3
"""
Définition d'une classe Rectangle avec les paramètres :
- width (largeur)
- height (hauteur)
La classe inclut des méthodes pour calculer l'aire et le périmètre,
ainsi que des représentations textuelles et des méthodes de comparaison.
"""


class Rectangle:
    """
    Classe Rectangle qui représente un rectangle.
    Attributs de classe :
        number_of_instances (int) : Nombre d'instances créées.
        print_symbol (str) : Symbole utilisé pour l'affichage du rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Args:
            width (int): La largeur du rectangle (par défaut 0).
            height (int): La hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retourne la largeur actuelle du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur actuelle du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """rectangle en utilisant `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbole = str(self.print_symbol)
        # Convertir en string pour éviter les erreurs
        rectangle = [symbole * self.__width for _ in range(self.__height)]
        return '\n'.join(rectangle)

    def __repr__(self):
        """rectangle qui permet de le recréer avec eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare les rectangles et revien le plus grand ou le premier

        Args:
            rect_1 (Rectangle): Premier rectangle à comparer.
            rect_2 (Rectangle): Deuxième rectangle à comparer.

        Returns:
            Rectangle: Le plus grand des deux rectangles ou rect_1 si égalité.

        Raises:
            TypeError:Si rect_1 ou rect_2,ne sont pas instances de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
