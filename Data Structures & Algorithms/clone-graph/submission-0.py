"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # store all unique nodes in a list
        # store node copies in a map
        
        # DFS thrugh the graph
        # if the neighbor is in seen, we skip it, otherwise we dfs on it
        if not node:
            return
        head = node
        nodes = set()
        cloneMap = dict()

        stk = [node]

        while stk:
            node = stk.pop()
            cloneMap[node.val] = Node(node.val)
            nodes.add(node)
            for nei in node.neighbors:
                if nei in nodes:
                    continue
                stk.append(nei)

        for node in nodes:
            clone = cloneMap[node.val]
            for nei in node.neighbors:
                clone.neighbors.append(cloneMap[nei.val])

        return cloneMap[head.val]
            
