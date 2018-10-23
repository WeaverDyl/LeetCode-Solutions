# Runtime 32 ms
# Beats 100% of Python submissions

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        mapping = {"1" : [],
                   "2" : ["a", "b", "c"],
                   "3" : ["d", "e", "f"],
                   "4" : ["g", "h", "i"],
                   "5" : ["j", "k", "l"],
                   "6" : ["m", "n", "o"],
                   "7" : ["p", "q", "r", "s"],
                   "8" : ["t", "u", "v"],
                   "9" : ["w", "x", "y", "z"],
                  }
        lst = [""]
        for num in digits:
            new = []
            for comb in lst:
                for letter in mapping[num]:
                    new.append(comb + letter)
            lst = new
        
        return lst