#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialise un compteur pour compter le nombre d'éléments affichés
    counter = 0
    try:
        # Parcourt les indices de 0 à x-1 pour afficher les éléments
        for i in range(0, x):
            # Affiche l'élément correspondant sans sauter de ligne
            print(my_list[i], end="")
            # Incrémente le compteur après chaque affichage réussi
            counter += 1
    except (IndexError, TypeError):
        # Ignore les exceptions si un indice est hors limite ou si la liste est invalide
        pass
    # Ajoute un saut de ligne après avoir affiché les éléments
    print()
    # Retourne le nombre total d'éléments affichés
    return counter
