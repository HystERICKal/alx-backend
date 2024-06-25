#!/usr/bin/env python3
"""Build a FIFO caching system."""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Build a FIFO caching system."""
    def __init__(self):
        """Build a FIFO caching system."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Build a FIFO caching system."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Build a FIFO caching system."""
        return self.cache_data.get(key, None)
