# Runtime: 28 ms
# Beats 100% of Python submissions

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_head = head
        while curr_head and curr_head.next:
            if curr_head.val == curr_head.next.val:
                curr_head.next = curr_head.next.next
            else:
                curr_head = curr_head.next
                
        return head