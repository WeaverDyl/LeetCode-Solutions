# Runtime: 48 ms
# Beats 100% of Python submissions

class Solution:
    def addDigits(self, num: 'int') -> 'int':
        new_num = (num // 10) + (num % 10)
        if new_num < 10:
            return new_num
        return self.addDigits(new_num)
