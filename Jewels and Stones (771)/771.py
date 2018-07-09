# Runtime: 24 ms
# Beats 99.35% of Python submissions

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for stone in S: # Go through each stone
            if stone in J: # Check if the stone is also a jewel
                res += 1 # increment if it it a jewel
        return res