# Runtime: 36 ms
# Beats 91.49% of Python submissions

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_of_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index_of_zero] = nums[index_of_zero], nums[i]
                index_of_zero += 1