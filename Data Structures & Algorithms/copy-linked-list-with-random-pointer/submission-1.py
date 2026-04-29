"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l1 = []
        l2 = []
        l1map = {}

        idx = 0
        curr = head
        while curr:
            l1.append(curr)
            l2.append(Node(curr.val))

            l1map[curr] = idx
            idx += 1
            curr = curr.next

        for idx in range(1, len(l2)):
            l2[idx - 1].next = l2[idx]
        
        for idx, node in enumerate(l2):
            l1random = l1[idx].random
            randomidx = l1map[l1random] if l1random else None       
            node.random = l2[randomidx] if l1random else None

        return l2[0] if len(l2) > 0 else None



