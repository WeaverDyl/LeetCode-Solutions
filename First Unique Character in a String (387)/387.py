# Runtime: 84 ms
# Beats 83.91% of Python submissions

from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        multiplicity = defaultdict(int)
        
        for letter in s:
            multiplicity[letter] += 1
            
        for index, letter in enumerate(s):
            if multiplicity[letter] == 1:
                return index
            
        return -1