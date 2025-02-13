#!/usr/bin/python3
"""
This module contains the read_file function
"""


def read_file(filename=""):
    """ Utiliser l'instruction 'with' pour ouvrir le fichier """
    with open(filename, "r", encoding="utf-8") as file:

        """end="" pour éviter une ligne vide supplémentaire"""
        print(file.read(), end="")
