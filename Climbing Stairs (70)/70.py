# Runtime: 20 ms
# Beats 97.04% of Python submissions

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [0] * (n + 1)
        return self.helper(n, lst)
    
    def helper(self, n, lst):
        lst[0], lst[1] = 1, 1
        for i in range(2, n + 1):
            lst[i] = (lst[i-1] + lst[i-2])
        return lst[n]
        