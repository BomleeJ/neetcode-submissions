# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 0 1 2 3 4 -> 0 4 1 3 2 
    # 0 1 2 3 -> 0 3 1 2
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Even (6) 6 / 2
        # Odd (7)

        # 0 1 2 3 4 5 | 6 7 8 9 NULL
        # 0 1 2 3 4 5 | 6 7 8 9 10

        # 0 1 2 3 4 | 5 6 7 8 NULL


        def reverse(head):
            prev = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev


        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next if fast.next else fast.next
            slow = slow.next
        
        newLast = slow

        rightHalfHead = reverse(newLast.next)

        slow.next = None

        rightcurr = rightHalfHead
        curr = head 

        while rightcurr:
            nextRight = rightcurr.next
            nextLeft = curr.next

            curr.next = rightcurr
            rightcurr.next = nextLeft

            curr = nextLeft
            rightcurr = nextRight
