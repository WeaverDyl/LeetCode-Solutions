# Runtime: 56 ms
# Beats 79.96% of Python submissions

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for letter in ransomNote:
            if magazine_count[letter] < ransom_count[letter]:
                return False
        return True
        