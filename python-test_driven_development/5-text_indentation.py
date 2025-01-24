#!/usr/bin/python3
"""
Imprime un texte avec des retours à la ligne après certains caractères.
Les caractères spéciaux sont : . , ? et :
"""

def text_indentation(text):
    """
    La fonction imprime le texte, ajoutant une nouvelle ligne après les caractères
    . , ? et :
    """
    chara = [".", "?", ":"]  # Liste des caractères qui déclenchent un retour à la ligne
    # Vérification si le paramètre 'text' est une chaîne de caractères
    if not isinstance(text, str):
        raise TypeError("text must be a string")  # Si ce n'est pas une chaîne, on lève une exception

    # On parcourt chaque caractère du texte
    for t in range(len(text)):
        # Si le caractère est un de ceux dans 'chara', on imprime le caractère et une nouvelle ligne
        if text[t] in chara:
            print(text[t])  # Affiche le caractère (., ?, :)
            print("")  # Ajoute une ligne vide après le caractère
        # Si le caractère précédent était un des caractères spéciaux ou un espace, et que l'actuel est un espace
        elif (text[t-1] in chara or text[t-1] == " ") and text[t] == " ":
            pass  # On ignore cet espace, il n'est pas imprimé
        else:
            print(text[t], end="")  # Affiche le caractère sans saut de ligne
