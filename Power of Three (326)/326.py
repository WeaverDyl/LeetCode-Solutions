# Runtime: 456 ms
# Beats 59.32% of Python submissions

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        while n % 3 == 0:
            n = n // 3
        return n == 1


# Or, perhaps less intuitively:

# class Solution:
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         return n > 0 and 1162261467 % n == 0