# Runtime 32 ms
# Beats 96.23% of Python submissions

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res_num = []
        for number in range(left, right + 1):
            res = True
            num = number
            
            if not number % 10:
                continue
                
            while num > 0:
                digit = num % 10
                if not digit or number % digit:
                    res = False
                    break
                num = num / 10
                
                
            if res:
                res_num.append(number)
            
        
        return res_num
                
        