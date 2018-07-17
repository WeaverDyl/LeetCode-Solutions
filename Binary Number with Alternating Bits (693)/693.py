# Runtime: 20 ms
# Beats 100% of Python submissions

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 0:
            prev_bit = n & 1
            n = n >> 1
            curr_bit = n & 1
            if prev_bit == curr_bit:
                return False
            
        return True
