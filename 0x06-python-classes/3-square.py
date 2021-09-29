#!/usr/bin/python3
"""
3. Area of a square
"""
class Square:
    def __init__(self, size=0):
        """
        Write a class Square that defines a square by:
        (based on 2-square.py)
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return size * size