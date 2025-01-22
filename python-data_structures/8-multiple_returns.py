#!/usr/bin/python3
def multiple_returns(sentence):
    # Calcule la longueur de la chaîne sentence
    length = len(sentence)
    # Si la chaîne n'est pas vide, récupère le premier caractère
    if sentence:
        first_c = sentence[0]
    else:
        # Si la chaîne est vide, first_c est None
        first_c = None
    # Retourne un tuple avec la longueur et le premier caractère (ou None)
    return (length, first_c)
