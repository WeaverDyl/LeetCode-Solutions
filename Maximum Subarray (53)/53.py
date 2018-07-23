# Runtime: 48 ms
# Beats 83.05% of Python submissions

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high, curr_sum = nums[0], nums[0]
        
        for i in nums[1:]:
            curr_sum = max(i, curr_sum + i)
            high = max(high, curr_sum)
            
        return high
        