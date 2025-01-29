#!/usr/bin/python3
"""Définit une classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.
            position (tuple): Coordonnées de position (décalage horizontal et vertical).

        Raises:
            TypeError: Si size n'est pas un entier ou si position n'est pas un tuple de 2 entiers positifs.
            ValueError: Si size est négatif.
        """
        self.size = size  # Utilisation du setter pour validation
        self.position = position  # Utilisation du setter pour validation

    @property
    def size(self):
        """Récupère la taille actuelle du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré en s'assurant qu'elle est valide.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):  # Vérifie que size est un entier
            raise TypeError("size must be an integer")
        elif value < 0:  # Vérifie que size est positif ou nul
            raise ValueError("size must be >= 0")
        self.__size = value  # Stocke la valeur validée

    @property
    def position(self):
        """Récupère la position actuelle du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Modifie la position du carré en s'assurant qu'elle est valide.

        Args:
            value (tuple): Un tuple de 2 entiers positifs (x, y).

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Stocke la position validée

    def area(self):
        """Retourne l'aire actuelle du carré."""
        return self.__size * self.__size  # Calcul de l'aire (côté * côté)

    def my_print(self):
        """Affiche le carré avec le caractère '#' en respectant la position."""
        if self.__size == 0:
            print("")  # Affiche une ligne vide si la taille est 0
            return

        # Affiche les lignes vides correspondant au décalage vertical
        [print("") for _ in range(self.__position[1])]

        # Affiche le carré avec le décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
