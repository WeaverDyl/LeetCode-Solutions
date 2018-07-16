# Runtime: 84 ms
# Beats 100% of Python submissions

from collections import defaultdict

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = defaultdict(lambda:-1)
        

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.hashmap[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.hashmap[key]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.hashmap[key] = -1

# 224 ms implementation using no extra modules:
# (Beats 57.89% of Python submissions)
#
# class MyHashMap(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashmap = [-1] * 1000001
        

#     def put(self, key, value):
#         """
#         value will always be positive.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         self.hashmap[key] = value
        

#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         return self.hashmap[key]
        

#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         self.hashmap[key] = -1
