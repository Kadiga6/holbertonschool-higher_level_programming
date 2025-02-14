#!/usr/bin/python3
"""
Ce module contient la fonction to_json_string.
"""


def from_json_string(my_str):
    """
    Retourne un objet représenté par une chaîne JSON.

    Args:
        my_str (str): La chaîne JSON à convertir en objet Python.

    Returns:
        object: L'objet Python représenté par la chaîne JSON.
    """
    import json
    return json.loads(my_str)
