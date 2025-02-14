#!/usr/bin/python3
"""
Ce module contient la fonction save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier texte en utilisant une représentation JSON.

    Args:
        my_obj (any type): L'objet à écrire dans le fichier.
        filename (str): Le nom du fichier dans lequel écrire.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        """Convertit l'objet my_obj en une chaîne JSON et
        écrit cette chaîne dans le fichier ouvert.
        """
        return json.dumps(my_obj, file)
