#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        Public instance method: def area(self): that raises
        an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
