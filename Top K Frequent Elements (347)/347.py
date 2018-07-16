# Runtime: 40 ms
# Beats 97.49% of Python submissions

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        element_multiplicity = defaultdict(int)
        
        for num in nums:
            element_multiplicity[num] += 1
                
        res = sorted(element_multiplicity, key = lambda x: element_multiplicity[x])
        print(res)
        
        return sorted(res[-k:])