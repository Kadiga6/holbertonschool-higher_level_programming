#!/usr/bin/python3
"""
This module contains the read_file function
"""


def read_file(filename=""):
    # Utiliser l'instruction 'with' pour ouvrir le fichier
    with open(filename, "r", encoding="utf-8") as f:
        # Lire le contenu du fichier
        contenu = f.read()
        """end="" pour éviter une ligne vide supplémentaire"""
        print(f.read(), end="")
