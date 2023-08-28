#!/usr/bin/python3
"""
Basic dictionary LRU Cache
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Caching System"""
    def __init__(self) -> None:
        super().__init__()
        self.xlist = []

    def put(self, key, item):
        """put function"""
        if key and item:
            if self.cache_data.get(key):
                self.xlist.remove(key)
            self.cache_data[key] = item
            self.xlist.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.xlist[0]))
                if key in self.cache_data:
                    del(self.cache_data[self.xlist[0]])
                    self.xlist.pop(0)

    def get(self, key):
        """Get function"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

        
