#!/usr/bin/python3
""" définr une classe square """


class Square:
    """ Classe qui définit un carré. """

    def __init__(self, size=0):
        """ Initialisation du carré avec une taille optionnelle. """

        if not isinstance(size, int):
            """ Vérifie si size est un entier """
            raise TypeError("size must be an integer")
        if size < 0:
            """ Vérifie si size est négatif """
            raise ValueError("size must be >= 0")
        self.__size = size
        """ L'attribut de l'instance doit être initialisé """

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size * self.__size
