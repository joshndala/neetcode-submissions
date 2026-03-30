class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1

        return result