#!/usr/bin/python3
"""
    Fonction qui imprime le prénom et le nom de famille
"""

def say_my_name(first_name, last_name=""):
    """
    Fonction qui imprime "My name is {first_name} {last_name}"
    Le nom de famille est optionnel.
    """
    # Vérification que 'first_name' est une chaîne de caractères
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")  # Si ce n'est pas une chaîne, on lève une exception de type TypeError

    # Vérification que 'last_name' est une chaîne de caractères
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")  # Si ce n'est pas une chaîne, on lève une exception de type TypeError

    # Impression du message formaté avec le prénom et le nom de famille
    print("My name is {:s} {:s}".format(first_name, last_name))
