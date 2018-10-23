# Runtime: 60 ms
# Beats 99.52% of Python submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        res = None
        
        for i in range(k):
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res = root.val
                root = root.right
                
        return res