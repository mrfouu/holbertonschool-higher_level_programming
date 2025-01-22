#!/usr/bin/python3
def element_at(list, idx):
    # Vérifie si l'indice est négatif
    if idx < 0:
        return None
    # Récupère la longueur de la liste
    list_length = len(list)
    # Vérifie si l'indice est hors des limites de la liste
    if idx >= list_length:
        return None
    # Retourne l'élément de la liste à l'indice donné
    return list[idx]
