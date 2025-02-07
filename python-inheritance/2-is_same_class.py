#!/usr/bin/python3

"""
Module contenant la fonction is_same_class.

Cette fonction permet de vérifier si un objet est exactement
une instance d'une classe donnée.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance de la classe spécifiée.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est exactement une instance de a_class, sinon False.
    """
    return type(obj) is a_class
