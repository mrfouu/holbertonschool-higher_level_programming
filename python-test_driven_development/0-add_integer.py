#!/usr/bin/python3
"""
Fonction qui divise chaque élément de la matrice par le diviseur (div)
"""
def matrix_divided(matrix, div):
    """
     Fonction qui divise tous les éléments de la matrice par le diviseur (div)
    """
       # Vérifie si div est un nombre (entier ou flottant)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")  # Erreur si div n'est pas un nombre

    # Vérifie si div est égal à zéro (division par zéro non autorisée)
    if div == 0:
        raise ZeroDivisionError("division by zero")  # Erreur si div est zéro

    # Vérifie que toutes les lignes de la matrice ont la même longueur
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")  # Erreur si les lignes sont de tailles différentes

        # Vérifie que tous les éléments de la matrice sont des entiers ou des flottants
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")  # Erreur si un élément n'est ni entier ni flottant

    # Effectue la division et arrondit chaque résultat à 2 décimales
    return [[round(data / div, 2) for data in row] for row in matrix]
