# Runtime: 20 ms
# Beats 100% of Python solutions

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp_dict = {}
        
        for index, num in enumerate(nums):
            complement_needed = target - num
            if complement_needed in comp_dict:
                return [comp_dict[complement_needed], index]
            else:
                comp_dict[num] = index