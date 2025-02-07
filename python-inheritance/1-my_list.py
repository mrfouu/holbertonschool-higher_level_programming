#!/usr/bin/python3

"""
Module définissant la classe MyList.

Cette classe hérite de `list` et ajoute une méthode pour afficher
une version triée de la liste.
"""


class MyList(list):
    """
    Classe MyList, une sous-classe de `list`.

    Cette classe ajoute une méthode `print_sorted` qui affiche la liste
    triée sans modifier l'ordre original.
    """

    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant.
        """
        print(sorted(self))
