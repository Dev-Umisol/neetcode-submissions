class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, col = len(grid), len(grid[0])
        perim = 0

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 1:
                    perim += 4

                    if r > 0 and grid[r-1][c] == 1:
                        perim -= 2
                    
                    if c > 0 and grid[r][c-1] == 1:
                        perim -= 2
        return perim