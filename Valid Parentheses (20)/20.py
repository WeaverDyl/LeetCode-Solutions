# Runtime: 24 ms
# Beats 81.68% of Python submissions

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }
        
        stack = []
        
        for parentheses in s:
            if not stack:
                stack.append(parentheses)
                continue
            elif stack[len(stack) - 1] in lookup:
                if lookup[stack[len(stack) - 1]] == parentheses:
                    stack.pop()
                    continue

            stack.append(parentheses)
                
        return not stack
    