# Question: https://leetcode.com/problems/reverse-linked-list-ii/submissions/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        for i in range(left-1):
            leftPrev, curr = curr, curr.next
        
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next
        
# Verdict:
# Runtime: 54 ms, faster than 35.47% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.2 MB, less than 18.38% of Python3 online submissions for Reverse Linked List II.
