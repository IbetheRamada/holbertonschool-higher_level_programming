#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""



class MyList(list):
    """
    A list inheritor
    """
    def __init__(self):
        """
        class initializer
        """
        super().__init__()
    def print_sorted(self):
        """
        Print the list
        """
        print(sorted(self))
