#!/usr/bin/python3
"""
Le programme définit des formes géométriques : 
- Triangle avec hauteur et largeur
- Cercle avec rayon
- shape_info pour imprimer l'aire et le périmètre
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.
    """
    @abstractmethod
    def area(self):
        """
        Méthode abstraite qui calcule l'aire de la forme.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Méthode abstraite qui calcule le périmètre de la forme.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.
    """
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        """
        Calcul de l'aire du cercle.
        """
        return (self.__radius ** 2) * math.pi

    def perimeter(self):
        """
        Calcul du périmètre du cercle.
        """
        return self.__radius * math.pi * 2


class Rectangle(Shape):
    """
    Classe représentant un rectangle.
    """
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        """
        Calcul de l'aire du rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calcul du périmètre du rectangle.
        """
        return (self.__height * 2) + (self.__width * 2)


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d'une forme géométrique.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
