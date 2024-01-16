#!/usr/bin/env python3
""" Implementing the MRU caching policy(algorithm) """


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ Caching system class """
    def __init__(self):
        """ calls the init method of the parent """
        super().__init__()
        self.freq_used = []

    def put(self, key, item):
        """ discards values from the cache using the MRU strategy """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.freq_used:
                self.freq_used.append(key)
            else:
                self.freq_used.append(
                    self.freq_used.pop(self.freq_used.index(key)))
            if len(self.freq_used) > BaseCaching.MAX_ITEMS:
                least_used = self.freq_used.pop(-2)
                del self.cache_data[least_used]
                print(f"DISCARD: {least_used}")
        else:
            return None

    def get(self, key):
        """  return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data.keys():
            self.freq_used.append(self.freq_used.pop(
                self.freq_used.index(key)
            ))
            return self.cache_data.get(key)
