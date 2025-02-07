#!/usr/bin/env python3
"""
Le programme crée une classe CountedIterator qui permet de compter
le nombre d'éléments itérés.
"""


class CountedIterator:
    """
    La classe CountedIterator permet de créer un itérateur qui compte
    le nombre d'éléments itérés.

    Attributs:
        iterator (iter): Un itérateur à partir de la séquence donnée.
        __count (int): Le compteur du nombre d'éléments itérés.
    """

    def __init__(self, item):
        """
        Initialise l'itérateur et le compteur.

        Args:
            item (iterable): Une séquence à itérer.
        """
        self.iterator = iter(item)
        self.__count = 0

    def __next__(self):
        """
        Retourne le prochain élément de l'itérateur et incrémente le compteur.

        Returns:
            object: Le prochain élément de l'itérateur.

        Raises:
            StopIteration: Si tous les éléments ont été itérés.
        """
        item = next(self.iterator)
        self.__count += 1
        return item

    def get_count(self):
        """
        Retourne le nombre d'éléments itérés jusqu'à présent.

        Returns:
            int: Le compteur des éléments itérés.
        """
        return self.__count
