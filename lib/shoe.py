#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # Calls the setter for size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):  # Ensures size is an integer
            self._size = size
        else:
            print("size must be an integer")
            self._size = None  # Set to None if the size is invalid

    def cobble(self):
        '''Method to simulate repairing the shoe'''
        print("Your shoe is as good as new!")
        self.condition = "New"  # After cobbling, the shoe's condition is "New"
