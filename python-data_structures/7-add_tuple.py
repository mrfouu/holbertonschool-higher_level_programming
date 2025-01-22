#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Vérifie si tuple_a a un premier élément, sinon utilise 0
    if len(tuple_a):
        a_1 = tuple_a[0]
    else:
        a_1 = 0
    # Vérifie si tuple_b a un premier élément, sinon utilise 0
    if len(tuple_b):
        b_1 = tuple_b[0]
    else:
        b_1 = 0
    # Vérifie si tuple_a a un deuxième élément, sinon utilise 0
    if len(tuple_a) > 1:
        a_2 = tuple_a[1]
    else:
        a_2 = 0
    # Vérifie si tuple_b a un deuxième élément, sinon utilise 0
    if len(tuple_b) > 1:
        b_2 = tuple_b[1]
    else:
        b_2 = 0
    # Retourne un tuple contenant la somme des éléments correspondants
    return (a_1 + b_1, a_2 + b_2)
