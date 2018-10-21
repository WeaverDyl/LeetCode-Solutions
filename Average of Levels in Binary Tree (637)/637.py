# Runtime: 64 ms
# Beats 82.64% of Python submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        lst = []
        queue = [root]
        
        while queue:
            curr_sum = 0
            count = len(queue)
            for _ in range(len(queue)):
                curr = queue.pop(0)
                curr_sum = curr_sum + curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            lst.append(curr_sum / count)
            
        return lst
		