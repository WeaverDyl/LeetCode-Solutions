# Runtime: 60 ms
# Beats 98.68% of Python submissions

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret_matrix = []

        for i in range(len(A[0])):
            subset = []
            for j in range(len(A)):
                subset.append(A[j][i])
            ret_matrix.append(subset)
                
        return ret_matrix
        