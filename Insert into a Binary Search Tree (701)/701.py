# Runtime: 128 ms
# Beats 99.53% of Python submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr_root = root
        
        if not curr_root:
            root = TreeNode(val)
            return root
        
        while curr_root: 
            if curr_root.val > val:
                if curr_root.left:
                    curr_root = curr_root.left
                else:
                    curr_root.left = TreeNode(val)
                    return root
            else:
                if curr_root.right:
                    curr_root = curr_root.right
                else:
                    curr_root.right = TreeNode(val)
                    return root
                
        return root
        