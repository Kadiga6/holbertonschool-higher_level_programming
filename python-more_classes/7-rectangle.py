#!/usr/bin/python3
"""Définition d'une classe Rectangle."""


class Rectangle:
    """Classe qui définit un rectangle."""

    # Attributs de classe
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur """
        """ Initialise un rectangle avec une hauteur optionnelle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retourne la largeur du rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Si width n'est pas un entier"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """Si width est négatif"""
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Si height n'est pas un entier"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """Si height est négatif"""
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation du rectangle print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for i in range(self.__height)])

    def __repr__(self):
        """Retourne une chaîne représentant l'objet rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Message lors de la suppression de l'instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
