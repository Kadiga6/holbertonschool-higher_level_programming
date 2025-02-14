#!/usr/bin/python3
"""
Ce module contient la fonction load_from_json_file
"""


def load_from_json_file(filename):
    """
    Crée un objet à partir d'un fichier JSON.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        object: L'objet Python représenté par le fichier JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
