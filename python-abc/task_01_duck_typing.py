#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite Shape avec les méthodes area et perimeter."""

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre."""
        pass


class Circle(Shape):
    """Classe représentant un cercle, héritant de Shape."""

    def __init__(self, radius):
        """Initialisation du cercle avec son rayon."""
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Retourne le périmètre du cercle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Classe représentant un rectangle, héritant de Shape."""

    def __init__(self, width, height):
        """Initialisation du rectangle avec sa largeur et sa hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme."""
    print(f"Aire: {shape.area()}")
    print(f"Périmètre: {shape.perimeter()}")
