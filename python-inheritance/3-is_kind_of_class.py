#!/usr/bin/python3

"""
Module contenant la fonction is_kind_of_class.

Cette fonction permet de vérifier si un objet est une instance
d'une classe donnée ou d'une classe dérivée.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe ou d'une classe héritée.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est une instance de a_class ou d'une classe dérivée, sinon False.
    """
    return isinstance(obj, a_class)
