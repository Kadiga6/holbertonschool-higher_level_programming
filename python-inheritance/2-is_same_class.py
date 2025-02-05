#!/usr/bin/python3


def is_same_class(obj, a_class):

    """Vérifie si l'objet est une instance exacte de la classe a_class"""
    if type(obj) is a_class:
        """Si l'objet est exactement de la classe a_class, retourne True"""
        return True
    """Sinon, retourne False"""
    return False
