# Runtime: 140 ms
# Beats 96.01% of Python submissions

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        go = 1
        
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[go] % 2 != 0:
                    go += 2
                A[i], A[go] = A[go], A[i]
        return A
        