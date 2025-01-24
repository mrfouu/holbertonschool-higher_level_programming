#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Essaie de diviser 'a' par 'b'
        azer = a / b
    except (ZeroDivisionError):
        # Si une division par zéro se produit, assigne None à 'azer'
        azer = None
    finally:
        # Affiche toujours le résultat (ou None si une erreur est survenue)
        print("Inside result: {}".format(azer))
        # Retourne la valeur calculée ou None en cas d'erreur
        return azer
