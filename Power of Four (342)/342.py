# Runtime: 56 ms
# Beats 72.71% of Python submissions

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 1010101010101010101010101010101 == 1431655765
        return bool(num) and num & (num - 1) == 0 and num & 1431655765 == num
