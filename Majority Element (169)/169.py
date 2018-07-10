# Runtime: 32 ms
# Beats 99.36% of Python submissions

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_multiplicity = {}
        
        for num in nums:
            if num not in element_multiplicity:
                element_multiplicity[num] = 1
            else:
                element_multiplicity[num] += 1
                
        return max(element_multiplicity, key=element_multiplicity.get)