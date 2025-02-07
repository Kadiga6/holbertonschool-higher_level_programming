#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Méthode abstraite que chaque sous-classe doit implémenter."""
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


"""Création d'un chien et d'un chat"""
dog = Dog()
cat = Cat()

"""Affichage du son de chaque animal"""
print(dog.sound())  # Doit afficher "Bark"
print(cat.sound())  # Doit afficher "Meow"
