# Runtime: 40 ms
# Beats 91.26% of Python submissions

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        current, maximum = 0, 0
        seen_first = False

        while N != 0:
            if N & 1:
                if not seen_first:
                    seen_first = True
                    current = 1
                else:
                    if current > maximum:
                        maximum = current
                    current = 1
            else:
                current += 1
            N = N >> 1
                
        return maximum