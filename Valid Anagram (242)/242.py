# Runtime: 32 ms
# Beats 97.02% of Python submissions (the fastest response that works for unicode as well)

from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        
        for letter in s:
            dict_s[letter] += 1
            
        for letter in t:
            dict_t[letter] += 1
            
        if dict_s == dict_t:
            return True
        else:
            return False