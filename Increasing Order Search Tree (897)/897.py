# Runtime: 156 ms
# Beats 72.62% of Python submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        lst = []
        lst = self.get_inorder(root, lst)
        if lst:
            root_ret = TreeNode(lst[0])
            root_backup = root_ret
            if len(lst) > 1:
                for elem in lst[1:]:
                    root_ret.right = TreeNode(elem)
                    root_ret = root_ret.right
        
        return root_backup
    
    def get_inorder(self, root, lst):
        if root:
            self.get_inorder(root.left, lst)
            lst.append(root.val)
            self.get_inorder(root.right, lst)
        
        return lst