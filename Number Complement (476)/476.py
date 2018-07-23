# Runtime: 20 ms
# Beats 100% of Python submissions

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        
        while i < num:
            i = i << 1 | 1
            
        return i ^ num