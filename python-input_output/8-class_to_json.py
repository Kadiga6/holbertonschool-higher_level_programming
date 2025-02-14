#!/usr/bin/python3
"""
Ce module contient la fonction class_to_json.py
"""


def class_to_json(obj):
    """
    Retourne la description du dictionnaire
    avec une structure de données simple
    pour la sérialisation JSON d'un objet.

    Args:
        obj (any): Une instance de classe
        dont les attributs doivent être sérialisés.

    Returns:
        dict: Un dictionnaire avec les attributs sérialisables de l'objet.
    """
    return obj.__dict__
