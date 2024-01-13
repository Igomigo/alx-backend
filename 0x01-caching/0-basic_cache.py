#!/usr/bin/python3
"""
Contains a class BasicCache that inherits from BaseCaching
and is a caching system.
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache class """
    def __init__(self):
        """ Initializes the class with the parent class init """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data
        the item value for the key """
        if key is None and item is None:
           pass
        else:
           self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
