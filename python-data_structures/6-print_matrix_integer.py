#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Vérifie si la matrice n'est pas vide
    if matrix:
        # Parcourt chaque ligne (chaque élément de la matrice)
        for row in matrix:
            # Si la ligne est vide, on affiche une ligne vide
            if not len(row):
                print()
            # Parcourt chaque élément de la ligne
            for i, elem in enumerate(row):
                # Affiche lélément actuel de la ligne avec le formatage demandé
                print("{:d}".format(row[i]), end="")
                # Si l'élément actuel n'est pas le dernier de la ligne
                if i is not len(row) - 1:
                    print(" ", end="")
                # Si l'élément actuel est le dernier de la ligne
                else:
                    print()
