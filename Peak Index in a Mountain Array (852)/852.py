# Runtime: 36 ms
# Beats 100% of Python submissions

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo, hi = 0, len(A) - 1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        
        return lo