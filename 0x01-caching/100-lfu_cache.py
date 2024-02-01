#!/usr/bin/python3
""" LFUCache module to work with a basic dictionary using LFU algorithm.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and
    is a caching system using LFU algorithm.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        dict_data = self.cache_data
        if len(dict_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, discard the least frequency used item (LFU)
            lfu_keys = [
            k for k, v in self.frequency.items() if v == min(self.frequency.values())
            ]   
            if len(lfu_keys) > 1:
                # If more than 1 item to discard, use LRU algo to discard LRU
                lfu_key = self.order_used.pop(0)
            else:
                lfu_key = lfu_keys[0]
            del dict_data[lfu_key]
            del self.frequency[lfu_key]
            print("DISCARD:", lfu_key)

        # Add the new item to the cache and update frequency
        dict_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        # Update frequency to indicate recent usage
        self.frequency[key] += 1

        return dict_data[key]
