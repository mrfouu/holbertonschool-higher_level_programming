#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    # Vérifie si la liste n'est pas vide
    if list:
        # Calcule la longueur de la liste pour définir les indices
        list_length = len(list)
        # Parcourt la liste en commençant par le dernier élément
        for i in range(list_length - 1, -1, -1):
            print("{:d}".format(list[i]))
    else:
        # Si la liste est vide, aucune action n'est effectuée
        pass
