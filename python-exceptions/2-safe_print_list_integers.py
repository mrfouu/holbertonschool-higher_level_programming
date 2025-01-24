#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Essaie d'afficher la valeur comme un entier
        print("{:d}".format(value))
    except (ValueError, TypeError):
        # Si une exception ValueError ou TypeError est levée, retourne False
        return False
    else:
        # Si aucune exception n'est levée, retourne True
        return True
