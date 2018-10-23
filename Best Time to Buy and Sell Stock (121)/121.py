# Runtime: 40 ms
# Beats 99.85% of Python submissions

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_so_far = 0
        
        for num in prices:
            if num < min_so_far:
                min_so_far = num
            elif num - min_so_far > max_so_far:
                max_so_far = num - min_so_far
                
        return max_so_far    