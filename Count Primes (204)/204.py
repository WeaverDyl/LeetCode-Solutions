# Runtime: 664 ms
# Beats 43.45% of Python submissions

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for i in range(n + 1)]
        
        check = 2
        num_primes = 0
        while check * check <= n:
            if primes[check]:
                for i in range(check * 2, n + 1, check):
                    primes[i] = False
            check += 1
            
        for i in range(2, n):
            if primes[i]:
                num_primes += 1
        
        return num_primes