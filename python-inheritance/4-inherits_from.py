#!/usr/bin/python3

"""
Module contenant la fonction inherits_from.

Cette fonction permet de vérifier si un objet est une instance
d'une classe qui hérite (directement ou indirectement) d'une autre classe,
sans être une instance directe de cette dernière.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une sous-classe donnée.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est une instance d'une sous-classe de a_class,
              mais pas une instance directe de a_class. Sinon, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
