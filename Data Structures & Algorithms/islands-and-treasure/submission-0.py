class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # filter for where zeros a
        # at each level enque the cells level by level

        INF = 2147483647
        from collections import deque
        que = deque([])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    que.append((y, x))

        def addValidNeighbors(y, x, que):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                nX = x + dx[i]
                nY = y + dy[i]
                inBounds = nY in range(len(grid)) and nX in range(len(grid[0]))
                if inBounds and grid[nY][nX] == INF:
                    que.appendleft((nY, nX))

        ZeroDist = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while que:
            sz = len(que)
            
            for i in range(sz):
                y, x = que.pop()
                grid[y][x] = min(ZeroDist, grid[y][x])
                addValidNeighbors(y, x, que)

            ZeroDist += 1



