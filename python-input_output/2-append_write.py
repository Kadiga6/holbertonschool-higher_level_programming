#!/usr/bin/python3
"""
This module contains the append_file function
"""


def append_write(filename="", text=""):
    """Utiliser l'instruction 'with' pour ouvrir le fichier en mode ajouter"""
    with open(filename, 'a', encoding='utf-8') as file:
        """Écrire le texte dans le fichier"""
        file.write(text)
    """Retourner le nombre de caractères écrits"""
    return len(text)
