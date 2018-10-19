# Runtime: 68 ms
# Beats 60.79% of Python submissions

class Solution():
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(A) - 1
        
        while l < r:
            while l < len(A) and A[l] % 2 == 0:
                l += 1
            while r >= 0 and A[r] % 2 == 1:
                r -= 1
            
            if l < r:
                A[l], A[r] = A[r], A[l]
                
        return A