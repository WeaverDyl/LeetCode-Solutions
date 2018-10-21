# Runtime: 176 ms
# Beats 77.94% of Python submissions

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        curr_max, max_index = self.max(nums)
        
        root = TreeNode(curr_max)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        
        return root
        
    def max(self, nums):
        curr_max = nums[0]
        max_index = 0
        
        for i in range(1, len(nums)):
            if nums[i] > curr_max:
                curr_max = nums[i]
                max_index = i
        
        return curr_max, max_index
        
        