#!/usr/bin/python3
""" Implementing the LIFO cacching policy(algorithm) """


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system class """
    def __init__(self):
        """ calls the init method of the parent """
        super().__init__()

    def put(self, key, item):
        """ discards values from the cache using the LIFO strategy """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                # LIFO data eviction algorithm
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item

    def get(self, key):
        """  return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
