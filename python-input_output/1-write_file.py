#!/usr/bin/python3

"""
This module contains the write_file function
"""


def write_file(filename="", text=""):
    """Utiliser l'instruction 'with' pour ouvrir le fichier"""
    with open(filename, "w", encoding='utf-8') as file:
        """ Écrire le texte dans le fichier """
        num_chars = file.write(text)
    """Retourner le nombre de caractères écrits"""
    return num_chars
