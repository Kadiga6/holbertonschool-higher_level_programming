#!/usr/bin/python3
"""
This module contains the JSON_file function
"""


def to_json_string(my_obj):
    """
    Retourne la représentation JSON d'un objet (chaîne de caractères).

    Args:
        my_obj (any type): L'objet à convertir en JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """
    import json
    return json.dumps(my_obj)
