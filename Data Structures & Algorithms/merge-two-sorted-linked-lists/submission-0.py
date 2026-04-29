# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1ptr = list2
        l2ptr = list1
        head = ListNode(-600)
        curr = head

        while l1ptr and l2ptr:
            if l1ptr.val > l2ptr.val:
                curr.next = ListNode(l2ptr.val)
                l2ptr = l2ptr.next
            else:
                curr.next = ListNode(l1ptr.val)
                l1ptr = l1ptr.next
            curr = curr.next

        remaining = l1ptr if l1ptr else l2ptr
        
        while remaining:
            curr.next = ListNode(remaining.val)
            remaining = remaining.next
            curr = curr.next

        return head.next

        
                
            