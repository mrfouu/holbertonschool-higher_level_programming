#!/usr/bin/python3
def max_integer(list=[]):
    # Si la liste est vide, retourne None
    if not list or not len(list):
        return None
    # Initialise la variable max avec le premier élément de la liste
    max = list[0]
    # Parcourt chaque élément de la liste
    for num in list:
        # Si l'élément courant est plus grand que max, met à jour max
        if num > max:
            max = num
    # Retourne la valeur maximale trouvée
    return max
