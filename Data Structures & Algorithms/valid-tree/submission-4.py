class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Maximally Acyclic graph
        # edge = n - 1 for tree
        # otherwise we can do a dfs and detect cycles
        # if there are no cycles, the graph is a tree

        if len(edges) != n - 1:
            return False

        graph = { node:[] for node in range(n) }
        
        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)
            
        print(graph)
        stk = [0]
        seen = set()
        
        while stk:
            node = stk.pop()
            seen.add(node)
            
            for nei in graph[node]:
                if nei not in seen:
                    stk.append(nei) 
        print(len(seen))
        print(seen)
        return len(seen) == n

            