# Runtime: 108 ms
# Beats 95.72% of Python submissions

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = (num + 1) * [0]
        
        for i in range(1, num + 1):
            lst[i] = (i & 1) + lst[i >> 1]
            
        return lst