#!/usr/bin/python3
def replace_in_list(list, idx, element):
    # Vérification si l'indice est négatif
    if idx < 0:
        return list
    # Calcul de la longueur de la liste
    list_length = len(list)
    # Vérification si l'indice est hors des limites de la liste
    if idx >= list_length:
        return list
    # Remplacement de l'élément à l'indice donné par l'élément spécifié
    list[idx] = element
    # Retour de la liste après modification
    return list
