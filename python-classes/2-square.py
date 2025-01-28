#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):  # Vérifie si size est un entier
            raise TypeError("size must be an integer")
        if size < 0:  # Vérifie si size est négatif
            raise ValueError("size must be >= 0")
        self.__size = size  # Si tout est correct, attribue la valeur
