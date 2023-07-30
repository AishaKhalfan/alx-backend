#!/usr/bin/python3
"""
LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """PUT FUNCTION"""
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lastItem = list(self.cache_data.keys())[-1]
                print(f"DISCARD:{lastItem}")
                del(self.cache_data[lastItem])
            self.cache_data[key] = item

    def get(self, key):
        """Get function"""
        if key is None:
            return None
        elif key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
