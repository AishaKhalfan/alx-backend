#!/usr/bin/python3
"""
Basic dictionary MRU Cache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache Caching System"""
    def __init__(self) -> None:
        super().__init__()
        self.xlist = []

    def put(self, key, item):
        """put function"""
        if key and item:
            # if self.cache_data.get(key):
            #     self.xlist.remove(key)
            # self.cache_data[key] = item
            # self.xlist.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = self.xlist.pop()
                print("DISCARD: {}".format(last_item))
                del(self.cache_data[last_item])
            self.cache_data[key] = item
            self.xlist.append(key)

    def get(self, key):
        """Get function"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

        
