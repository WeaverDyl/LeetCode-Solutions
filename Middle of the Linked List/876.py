# Runtime: 32 ms
# Beats 99.87% of Python submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Could make one pass to find number of elements,
        # then traverse to the middle of that and return the
        # element there, but that's stupid.
        
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
        if not fast_ptr or not fast_ptr.next:
            return slow_ptr
        return slow_ptr.next
        