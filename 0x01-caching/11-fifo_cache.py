
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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the first item (FIFO) and its key to be discarded
                oldest_key = next(iter(self.cache_data))
                # Discard the oldest item   
                print(f"DISCARD:{oldest_key}")
                del(self.cache_data[oldest_key])

    def get(self, key):
        """Get value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cahe_data[key]
        # if key is not None:
        #     for k, value in self.cache_data.items():
        #         if k == key:
        #             return value
        # return None
        
