# Runtime: 24 ms
# Beats 100% of Python submissions

from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        bull, cow, secret_dict, guess_dict = 0, 0, defaultdict(int), defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                secret_dict[s] += 1
                guess_dict[g] += 1
        
        for key in guess_dict:
            cow += min(guess_dict[key], secret_dict[key])
            
        return str(bull) + "A" + str(cow) + "B"