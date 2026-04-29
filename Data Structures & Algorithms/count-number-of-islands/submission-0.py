class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def IslandRemove(Sx: int, Sy: int, grid: List[List[str]]):

            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

            def isValidLand(x: int, y: int, grid: List[List[str]]) -> bool:
                if (x in range(len(grid[0])) and y in range(len(grid))) and grid[y][x] == '1':
                    return True
                return False

            start = Point(Sx, Sy)
            stack = [start]

            dirx = [1, -1, 0, 0]
            diry = [0, 0, 1,-1]

            while stack:
                focus = stack.pop()

                for idx in range(4):
                    nX = focus.x + dirx[idx]
                    nY = focus.y + diry[idx]
                    if isValidLand(nX, nY, grid):
                        newLand = Point(nX, nY)
                        stack.append(newLand)
                        grid[nY][nX] = "0"

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    IslandRemove(x, y, grid)
                    count += 1

        return count
                

                    