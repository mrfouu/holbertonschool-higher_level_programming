#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Si l'index est négatif ou hors des limites de la liste, retourne la liste
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # Sinon, supprime l'élément à l'index spécifié
        del my_list[idx]
        # Retourne la liste modifiée
        return my_list
