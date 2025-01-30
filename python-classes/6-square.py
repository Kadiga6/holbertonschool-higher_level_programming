#!/usr/bin/python3
""" définr une classe square """


class Square:
    """ Initialisation du carré avec une taille optionnelle. """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Vérifie si size est un entier """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """ Vérifie si size est négatif """
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Vérifie si position est un tuple de 2 éléments
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Vérifie si les éléments de position sont des entiers et positifs
        if not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        """ Gérer les lignes initiales dues à position[1] """
        print("\n" * self.__position[1], end="")

        """ Gérer chaque ligne du carré """
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
