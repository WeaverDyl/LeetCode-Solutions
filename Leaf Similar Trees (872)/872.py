# Runtime: 36 ms
# Beats 99.34% of Python submissiona

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.dfs(root1, []) == self.dfs(root2, [])
        
    def dfs(self, root, lst):
        if root:
            if not root.left and not root.right:
                lst.append(root.val)
            self.dfs(root.left, lst)
            self.dfs(root.right, lst)
            
        return lst
       34% 