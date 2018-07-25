# Runtime: 60 ms
# Beats 84.04% of Python submissions

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        beginning = 0
        end = len(s) - 1
        s = s.lower()
        
        while beginning < end:
            if not s[beginning].isalnum():
                beginning += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[beginning] != s[end]:
                    return False
                beginning += 1
                end -= 1
        
        return True
        