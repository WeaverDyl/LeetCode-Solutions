# Runtime: 20 ms
# Beats 100% of Python submissions

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = []
        seen = []
        
        for word in words:
            string = ""
            
            for letter in word:
                string += alphabet[ord(letter) - 97]
            
            transformations.append(string)
            
        for transformation in transformations:
            if transformation not in seen:
                seen.append(transformation)
        
        return(len(seen))