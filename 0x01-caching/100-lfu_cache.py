#!/usr/bin/env python3
"""Build a LFU caching system."""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Build a LFU caching system."""
    def __init__(self):
        """Build a LFU caching system."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, temp_6):
        """Build a LFU caching system."""
        temp_1 = []
        temp_2 = 0
        temp_3 = 0
        temp_4 = 0
        for x, y in enumerate(self.keys_freq):
            if y[0] == temp_6:
                temp_2 = y[1] + 1
                temp_3 = x
                break
            elif len(temp_1) == 0:
                temp_1.append(x)
            elif y[1] < self.keys_freq[temp_1[-1]][1]:
                temp_1.append(x)
        temp_1.reverse()
        for z in temp_1:
            if self.keys_freq[z][1] > temp_2:
                break
            temp_4 = z
        self.keys_freq.pop(temp_3)
        self.keys_freq.insert(temp_4, [temp_6, temp_2])

    def put(self, key, item):
        """Build a LFU caching system."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            temp_8 = len(self.keys_freq)
            for x, y in enumerate(self.keys_freq):
                if y[1] == 0:
                    temp_8 = x
                    break
            self.keys_freq.insert(temp_8, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Build a LFU caching system."""
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
