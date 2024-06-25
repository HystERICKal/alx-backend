#!/usr/bin/env python3
"""Build a caching system."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Build a caching system."""
    def put(self, key, item):
        """Build a caching system."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Build a caching system."""
        return self.cache_data.get(key, None)
