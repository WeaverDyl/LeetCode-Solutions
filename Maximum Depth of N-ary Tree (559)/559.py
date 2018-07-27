# Runtime: 108 ms
# Beats 74.56% of Python submissions

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        res = 0
        if not root:
            return 0
        for child in root.children:
            res = max(res, self.maxDepth(child))
        return res + 1