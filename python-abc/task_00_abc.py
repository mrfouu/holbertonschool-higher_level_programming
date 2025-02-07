#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être définie dans les classes filles
        pour spécifier le son que fait l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien.
    """

    def sound(self):
        """
        Définit le son que fait un chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat.
    """

    def sound(self):
        """
        Définit le son que fait un chat.
        """
        return "Meow"
