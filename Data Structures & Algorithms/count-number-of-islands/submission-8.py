class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (r, c)
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        result = 0

        def dfs(r, c):
            if (r, c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r, c))
            
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1":
                    dfs(nr, nc)
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                
                dfs(r, c)
                result += 1

        return result