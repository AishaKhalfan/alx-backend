#!/usr/bin/env python3
"""
functools.lru_cache:
implements a Least Recently Used (LRU) cache.
This decorator automatically caches function results based
on the function's arguments, keeping only the most recently 
used items in the cache.
"""
from functools import lru_cache

@lru_cache(maxsize=None)  # Set maxsize to limit the cache size or None for unlimited size
def expensive_function(x):
    # Perform expensive computation here
    return x * x

print(expensive_function(2))
