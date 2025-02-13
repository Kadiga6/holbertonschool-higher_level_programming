#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        """end="" pour éviter une ligne vide supplémentaire"""
        print(f.read(), end="")
