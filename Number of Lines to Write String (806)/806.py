#
#

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        total_width = 0
        total_lines = 1
    
        for letter in S:
            curr_width = widths[ord(letter) - 97]
            total_width += curr_width
            if total_width > 100:
                total_lines += 1
                total_width = curr_width

        return [total_lines, total_width]