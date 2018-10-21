# Runtime: 36 ms
# Beats 99.62% of Python submissions

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret_arr = []
        
        for word in words:
            map1 = {}
            map2 = {}
            i = 0
            
            for letter in pattern:
                if word[i] not in map1:
                    map1[word[i]] = letter
                else:
                    if map1[word[i]] != letter:
                        break
                        
                if letter not in map2:
                    map2[letter] = word[i]
                else:
                    if map2[letter] != word[i]:
                        break
                
                i += 1
                
                if len(word) == i:
                    ret_arr.append(word)

                        
        return ret_arr