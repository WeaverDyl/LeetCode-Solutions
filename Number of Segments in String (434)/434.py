# Runtime: 20 ms
# Beats 98.05% of Python submissions

import re

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        if not s:
            return 0
        
        for word in re.split('\s+', s):
            if len(word) > 0:
                count += 1
        
        return count

# Or, more simply:
# import re

# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         return len(s.split())