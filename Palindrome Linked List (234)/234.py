# Runtime: 80 ms
# Beats 98.33% of Python submissions

from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = deque()
        curr_head = head

        while curr_head:
            rev.append(curr_head.val)
            curr_head = curr_head.next
            
        curr_head = head
        while curr_head:
            if rev.pop() != curr_head.val:
                return False
            curr_head = curr_head.next
            
        return True
        