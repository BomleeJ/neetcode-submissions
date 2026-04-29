# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1ptr, l2ptr, sump = l1, l2, ListNode(-600)
        sumptr = sump
        sumval = 0

        carry = 0 
        while l1ptr or l2ptr:
            l1val = l1ptr.val if l1ptr else 0
            l2val = l2ptr.val if l2ptr else 0

            total =  l1val + l2val + carry
            carry = total // 10
            sumptr.next = ListNode(total % 10)

            l1ptr = l1ptr.next if l1ptr else None
            l2ptr = l2ptr.next if l2ptr else None
            sumptr = sumptr.next

        if carry:
            sumptr.next = ListNode(1)

        return sump.next







        