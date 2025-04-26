#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # Calls the setter for page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):  # Ensures page_count is an integer
            self._page_count = count
        else:
            print("page_count must be an integer")
            self._page_count = None  # Set to None if the page_count is invalid

    def turn_page(self):
        '''Method to simulate turning a page'''
        print("Flipping the page...wow, you read fast!")
