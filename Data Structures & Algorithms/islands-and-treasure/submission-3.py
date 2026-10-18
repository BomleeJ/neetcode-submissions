from collections import deque
class Solution:
    
    def runBfs(self, que, visited, grid):
        """
        we can't vist out of bounds
        we can't vist cells -1 
        we can vist cells that are 0 <- 
        but shouldn't change them

        0 -> 1 -> 1 -> 0 -> 1 -> 1 ->1
        """
        def isValid(y, x):
            inBounds = 0 <= y and 0 <= x and y < len(grid) and x < len(grid[0])
            if not inBounds:
                return False
            
            if grid[y][x] == -1:
                return False
            
            if grid[y][x] == 0:
                return False

            return True


        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        dist = 0
        while que:
            lvlSz = len(que)
            for i in range(lvlSz):
                Y, X = que.pop()
                for idx in range(4):
                    nY = Y + dy[idx]
                    nX = X + dx[idx]
                    if (nY, nX) in visited:
                        continue

                    if not isValid(nY, nX):
                        continue 
                    
                    visited.add((nY, nX))
                    que.appendleft((nY, nX))
                
                    if grid[nY][nX] == 0:
                        continue
                    
                    grid[nY][nX] = dist+1
            dist += 1
        
        return None




    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        -1 = Water
        0 = chest <- minumum distance of each land to chests
        INF = land

        grid inplace replacing each INF with the minimum distance to a chest

        INF 

        [1,0,-1,-1,INF]

        BFS <- minimum distance

        find tresure chest, 
            run bfs 
            level_bfs 
                grid min(current, lvl)
        
        1. need to identify which are treasure chest
        2. run level BFS on each treasure chest (replacing grid inplace)
        3. return grid

        visitedSet

        bfs one level at a time 

        all the chests in the queue 
        
        """

        que = deque([])
        visited = set()
        width = len(grid[0])
        height = len(grid)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    que.appendleft((y,x))
                    visited.add((y,x))
        
        if not que:
            return None
        
        self.runBfs(que, visited, grid)
        
        
        
        
        """
        all chests should be the que

        lvl order traversal (vistiedSet)

        Isn't valid if it is 0, -1, OOB
        """
        
