#!/usr/bin/python3
"""
Fonction qui divise la matrice par un diviseur donné (div)
"""
def matrix_divided(matrix, div):
    """
    Fonction qui divise tous les éléments de la matrice par le diviseur (div)
    """
    # Vérification si le diviseur 'div' est un nombre (entier ou flottant)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")  # Si ce n'est pas un nombre, on lève une exception TypeError

    # Vérification si le diviseur est égal à zéro (division par zéro interdite)
    if div == 0:
        raise ZeroDivisionError("division by zero")  # Si div est zéro, on lève une exception ZeroDivisionError

    # Vérification que toutes les lignes de la matrice ont la même taille
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")  # Si les lignes sont de tailles différentes, on lève une exception

        # Vérification que chaque élément de la matrice est un entier ou un flottant
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix "
                                 "(list of lists) of integers/floats")  # Si un élément n'est ni un entier ni un flottant, on lève une exception

    # Division de chaque élément de la matrice par le diviseur et arrondi à 2 décimales
    return [[round(data / div, 2) for data in row] for row in matrix]  # Renvoie la matrice divisée avec les résultats arrondis
