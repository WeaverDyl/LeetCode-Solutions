# Runtime: 20 ms
# Beats 100% of Python submissions

import re

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = re.split(' ', s)
        curr_end_length = 0
        
        for index, word in enumerate(words):
            if index != len(words):
                if word != "":
                    curr_end_length = len(word)

        return curr_end_length