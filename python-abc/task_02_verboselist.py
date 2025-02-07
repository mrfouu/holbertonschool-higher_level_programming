#!/usr/bin/env python3
"""
Le programme crée une classe VerboseList :
- Hérite de la liste intégrée (built-in list)
- Redéfinit les méthodes append, extend, remove, pop pour afficher des messages détaillés
"""
class VerboseList(list):
    """
    Classe VerboseList qui hérite de la classe list.

    Cette classe redéfinit les méthodes append, extend, remove et pop
    pour afficher des messages chaque fois qu'une de ces opérations
    est effectuée sur la liste.
    """
    def append(self, item):
        """
        Ajoute un élément à la liste et affiche un message.

        Args:
            item (Any): L'élément à ajouter à la liste.
        """
        print("Added [{}] to the list".format(item))
        super().append(item)

    def extend(self, items):
        """
        Étend la liste avec les éléments donnés et affiche un message.

        Args:
            items (list): Liste d'éléments à ajouter à la liste.
        """
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """
        Supprime un élément de la liste et affiche un message.

        Args:
            item (Any): L'élément à supprimer de la liste.

        Raises:
            ValueError: Si l'élément n'est pas dans la liste.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Supprime un élément à un indice donné et affiche un message.

        Args:
            index (int, optional): L'indice de l'élément à supprimer. Par défaut, -1.

        Returns:
            Any: L'élément qui a été supprimé.

        Raises:
            IndexError: Si l'indice est hors de portée.
        """
        if len(self) == 0:
            print("The list is empty, cannot pop an item.")
            return None
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
