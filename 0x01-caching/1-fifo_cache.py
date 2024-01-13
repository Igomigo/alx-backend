#!/usr/bin/python3
""" Implementing the FIFO cacching policy(algorithm) """


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system class """

    def __init__(self):
        """ calls the init method of the parent """
        super().__init__()

    def put(self, key, item):
        """ Adds values to the cache using the FIFO strategy """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                # FIFO data eviction algorithm
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """  return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
