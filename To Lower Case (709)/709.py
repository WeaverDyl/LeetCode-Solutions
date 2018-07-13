# Runtime: 20 ms
# Beats ??% of Python submissions

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new = ""
        
        for letter in str:
            if ord(letter) in range(65, 91):
                new += chr(ord(letter) + 32)
            else:
                new += letter
            
        return new