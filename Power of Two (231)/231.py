# Runtime: 24 ms
# Beats 100% of Python submissions

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n == 0 else n & (n - 1) == 0