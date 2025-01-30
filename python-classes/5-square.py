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
        if not isinstance(value, int):
            """ Vérifie si size est un entier """
            raise TypeError("size must be an integer")
        if value < 0:
            """ Vérifie si size est négatif """
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ retourne l'aire """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
