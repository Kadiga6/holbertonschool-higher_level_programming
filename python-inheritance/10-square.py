#!/usr/bin/python3
"""Module définissant la classe Rectangle qui hérite de BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les géométries."""

    def area(self):
        """Lève une exception indiquant que l'aire n'est pas implémentée."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide la valeur en vérifiant qu'elle est un entier et > 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Classe représentant un rectangle, héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialisation avec validation des dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Retourne la description du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Classe représentant un carré, héritant de Rectangle."""

    def __init__(self, size):
        """Initialisation avec la validation de la taille."""
        self.integer_validator("size", size)
        """Appel à la méthode __init__ de Rectangle"""
        super().__init__(size, size)
