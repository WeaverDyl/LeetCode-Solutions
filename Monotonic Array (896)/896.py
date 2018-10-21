# Runtime: 92 ms
# Beats 98.03% of Python submissions

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        
        increasing = False
        decreasing = False
        
        for num in range(1, len(A)):
            if increasing:
                if A[num] < A[num - 1]:
                    return False
                continue
            if decreasing:
                if A[num] > A[num - 1]:
                    return False
                continue
                
            if A[num] > A[num - 1]:
                increasing = True
            elif A[num] < A[num - 1]:
                decreasing = True
            else:
                continue
        
        return True