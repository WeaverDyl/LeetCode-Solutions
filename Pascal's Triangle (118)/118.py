# Runtime: 36 ms
# Beats 91.64% of Python submissions

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        
        # Handle base case business
        if numRows == 0:
            return ret
        else:
            ret = [[1]]
        
        for curr in range(1, numRows):
            new_arr = [0] * (len(ret[curr - 1]) + 1) # Make list of correct length
            new_arr[0], new_arr[-1] = 1, 1 # Set edges
            
            # Set each sum in the new list
            for num in range(1, len(new_arr) - 1):
                new_arr[num] = ret[curr - 1][num - 1] + ret[curr - 1][num]
                
            ret.append(new_arr)
            
        return ret
        