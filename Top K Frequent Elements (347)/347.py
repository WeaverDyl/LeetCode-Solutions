# Runtime: 20 ms
# Beats 100% of Python submissions

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("LLL") > 0:
            return False
        if s.count("A") > 2:
            return False
        return True

# A more worked out solution is:
# class Solution(object):
#     def checkRecord(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         a_count = 0
#         cons_p_count = 0
        
#         for day in s:
#             if day == 'A':
#                 a_count +=1
#             if day == 'L':
#                 cons_p_count += 1
#             else:
#                 cons_p_count = 0
#             if a_count > 1:
#                 return False
#             if cons_p_count > 2:
#                 return False
        
#         return True