# Runtime: 20 ms
# Beats 100% of Python submissions

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words_array = []
        
        for index,word in enumerate(S.split()):
            end_a = (index + 1) * 'a'
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            words_array.append(word + end_a)
            
        return " ".join(words_array)