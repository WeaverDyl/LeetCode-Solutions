# Runtime: 40 ms
# Beats 67.42% of Python submissions

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0]) - 1
        for i in range(l):
            for j in range(l-i):
                matrix[i][j], matrix[l-j][l-i] = matrix[l-j][l-i], matrix[i][j]

        curr_row = len(matrix) - 1
        for i in range((l // 2) + 1):
            matrix[i], matrix[curr_row] = matrix[curr_row], matrix[i]
            curr_row -= 1
			