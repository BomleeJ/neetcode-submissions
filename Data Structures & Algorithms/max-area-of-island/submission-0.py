class Solution:
    def evalIsland(self, grid, x, y):
        inBounds = y in range(len(grid)) and x in range(len(grid[0]))
        if not inBounds:
            return 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        cell = grid[y][x]
        if cell != 1:
            return 0

        grid[y][x] = 0
        area = 0
        for i in range(4):
            nX = x + dx[i]
            nY = y + dy[i]
            tmp = self.evalIsland(grid, nX, nY)
            area += tmp
        
        return 1 + area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for y, row in enumerate(grid):
            for x in range(len(grid[0])):
                if row[x] == 1:
                    tmp = self.evalIsland(grid, x, y)
                    area = max(area, tmp)
            
        return area
        