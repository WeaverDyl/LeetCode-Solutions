# Runtime: 80 ms
# Beats 74% of Python submissions

# Worked out solution:
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        curr = 0
        for direction in moves:
            if direction == "U" or direction == "R":
                curr += 1
            else:
                curr -= 1
        return curr == 0

# The previous code is essentially checking this, which is much faster:

# Runtime: 28 ms
# Beats 84.58% of Python submissions

# class Solution(object):
#     def judgeCircle(self, moves):
#         """
#         :type moves: str
#         :rtype: bool
#         """
#         return moves.count('U') + moves.count('R') == moves.count('D') + moves.count('L')