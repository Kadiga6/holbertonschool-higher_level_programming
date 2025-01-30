#!/usr/bin/python3
""" définr une classe square """


class Square:
    """ Classe qui définit un carré. """

    def __init__(self, size=0):
        """ Initialisation du carré avec une taille optionnelle. """

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Vérifie si size est un entier """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            """ Vérifie si size est négatif """
            raise ValueError("size must be >= 0")
        self.__size = value
        """ Si tout est correct, attribue la valeur """

    def area(self):
        """ Retourne L'aire """
        return self.__size * self.__size
