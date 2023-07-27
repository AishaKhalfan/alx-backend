#!/usr/bin/env python3
# Example of a simple in-memory cache using a dictionary
cache = {}

def expensive_func(x):
    if x in cache:
        return cache[x]

    # Perform expensive computation here
    result = x * x
    
    # Cache the result
    cache[x] = result
    return result

print(expensive_func(2))
