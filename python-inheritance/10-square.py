#!/usr/bin/python3
"""Module définissant la classe Rectangle qui hérite de BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe représentant un carré, héritant de Rectangle."""

    def __init__(self, size):
        """Initialisation avec la validation de la taille."""
        self.integer_validator("size", size)
        """Appel à la méthode __init__ de Rectangle"""
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Retourne l'aire du carré"""
        return (self.__size * self.__size)
