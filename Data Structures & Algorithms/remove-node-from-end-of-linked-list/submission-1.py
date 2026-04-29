# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                Next = curr.next
                curr.next = prev
                prev = curr
                curr = Next
            return prev
        
        newHead = reverse(head)
        prev, curr = None, newHead
        for i in range(1, n):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next #assumes curr.next exists
        else:
            newHead = newHead.next

        return reverse(newHead)