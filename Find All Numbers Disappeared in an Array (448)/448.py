# Runtime: 184 ms
# Beats 65.77% of Python submissions

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        
        for num in range(len(nums)):
            index = abs(nums[num]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            
        for i in range(len(nums)):
            if nums[i] > 0:
                lst.append(i + 1)
                
        return lst