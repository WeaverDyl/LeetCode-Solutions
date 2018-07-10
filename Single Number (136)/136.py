class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            # xoring each number will live you with the only non-duplicate
            result ^= i
        return result

        # Other solutions using sets or dicts can be made with O(n) space