#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Initialise une nouvelle liste pour stocker les résultats
    azerty = []
    for i in range(0, list_length):
        try:
            # Essaie de diviser les éléments des deux listes
            azerty.append(my_list_1[i] / my_list_2[i])
        except (TypeError):
            # Gère les erreurs de type (par exemple, un élément n'est pas un nombre)
            print("wrong type")
            azerty.append(0)
        except (ZeroDivisionError):
            # Gère la division par zéro
            print("division by 0")
            azerty.append(0)
        except (IndexError):
            # Gère les cas où un indice dépasse la taille d'une des listes
            print("out of range")
            azerty.append(0)
        finally:
            # Le bloc `finally` est exécuté à chaque itération, ici il est vide
            pass
    # Retourne la liste des résultats
    return azerty
