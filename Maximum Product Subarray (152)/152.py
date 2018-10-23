# Runtime: 56 ms
# Beats 55.18% of Python submissions

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_total = nums[0]
        min_last = nums[0]
        max_last = max_total
        
        for num in nums[1:]:
            max_temp = max(num, max(max_last * num, min_last * num))
            min_temp = min(num, min(max_last * num, min_last * num))
            
            max_last = max_temp
            min_last = min_temp
            
            max_total = max(max_last, max_total)
            
        return max_total
