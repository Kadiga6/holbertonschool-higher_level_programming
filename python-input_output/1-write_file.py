#!/usr/bin/python3

"""
Écrit une chaîne de caractères dans un fichier texte UTF-8 et retourne le nombre de caractères écrits.

    Args:
        filename (str): Le nom du fichier dans lequel écrire.
        text (str): La chaîne de caractères à écrire dans le fichier.

    Returns:
        int: Le nombre de caractères écrits dans le fichier.
"""

def write_file(filename="", text=""):
    """Utiliser l'instruction 'with' pour ouvrir le fichier"""
    with open(filename, "w", encoding='utf-8') as file:
        """ Écrire le texte dans le fichier """
        num_chars = file.write(text)
    """Retourner le nombre de caractères écrits"""
    return num_chars
