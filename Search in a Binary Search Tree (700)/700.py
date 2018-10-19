# Runtime: 92 ms
# Beats 79.07% of Python submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        else:
            while root:
                if root.val == val:
                    return root
                if root.val > val:
                    root = root.left
                else:
                    root = root.right
            return None

# Or, a slower (stupider) recursive solution:

# def searchBST(self, root, val):
    # """
    # :type root: TreeNode
    # :type val: int
    # :rtype: TreeNode
    # """
    # if not root:
    #     return []
    # else:
    #     while root:
    #         if root.val == val:
    #             return root
    #         if root.val > val:
    #             return self.searchBST(root.left, val)
    #         else:
    #             return self.searchBST(root.right, val)
    #     return None