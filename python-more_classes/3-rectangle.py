#!/usr/bin/python3
"""Définition d'une classe Rectangle."""


class Rectangle:
    """Classe qui définit un rectangle."""

    def __init__(self, width=0, height=0):
        """ Initialise un rectangle avec une largeur """
        """ Initialise un rectangle avecune hauteur optionnelles """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retourne la largeur du rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Si width n'est pas un entier """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """ Si width est négatif """
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retourne la hauteur du rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Si height n'est pas un entier """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """ Si height est négatif """
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Retourne l'aire d'un rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Retourne le périmètre du rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Affiche le rectangle avec le caractère # """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])
