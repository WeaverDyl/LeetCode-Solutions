# Runtime: 20 ms
# Beats 94.44% of Python submissions

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            middle = (left + right) // 2
            
            if guess(middle) > 0:
                left = middle + 1
            elif guess(middle) < 0:
                right = middle - 1
            else:
                return middle