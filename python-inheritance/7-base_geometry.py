#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry():
    """Empty class BaseGeometry"""
    def area(self):
        """raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value
        Args:
            name: a string
            value: Value of geometry
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
