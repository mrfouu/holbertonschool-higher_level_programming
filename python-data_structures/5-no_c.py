#!/usr/bin/python3
def no_c(my_string):
    # Initialise une nouvelle chaîne vide pour stocker les résultats
    new_string = ""
    # Parcourt chaque caractère de la chaîne d'entrée
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            new_string += i
    # Retourne la chaîne modifiée
    return new_string
