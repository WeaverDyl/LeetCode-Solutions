# Runtime: 40 ms
# Beats 99% of Python submissions

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s_t = {}
        map_t_s = {}
        
        for let1, let2 in zip(s, t):
            if let1 not in map_s_t:
                map_s_t[let1] = let2
            if let2 not in map_t_s:
                map_t_s[let2] = let1
            if map_s_t[let1] != let2 or map_t_s[let2] != let1:
                return False
                
        return True
            
        