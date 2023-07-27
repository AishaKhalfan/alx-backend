from cachetools import cached, TTLCache

@cached(cache=TTLCache(maxsize=100, ttl=3600))  # Set maxsize for cache size and ttl for time-to-live (in seconds)
def expensive_function(x):
    # Perform expensive computation here
    return x * x
