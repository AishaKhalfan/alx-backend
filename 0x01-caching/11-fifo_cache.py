
#!/usr/bin/python3
"""
FIFO caching
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Put function definition"""
        if key and item:
            self.cache_data[key] = item
        
