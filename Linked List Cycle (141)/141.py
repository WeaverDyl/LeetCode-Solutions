# Runtime: 44 ms
# Beats 96.03% of Python submissions

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        else:
            slow, fast = head, head.next
            while slow != fast:
                if fast is None or fast.next is None:
                    return False
                slow = slow.next
                fast = fast.next.next
            return True
			