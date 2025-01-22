#!/usr/bin/python3
def divisible_by_2(list=[]):
    # Crée une copie de la liste list pour ne pas modifier l'originale
    truth_list = list[:]
    # Parcourt chaque élément de list avec son index
    for i, num in enumerate(list):
        # Si l'élément est divisible par 2, mettre True dans truth_list
        if num % 2 == 0:
            truth_list[i] = True
        else:
            # Si l'élément n'est pas divisible par 2, mettre False
            truth_list[i] = False
    # Retourne la liste des résultats True/False pour chaque élément
    return truth_list
