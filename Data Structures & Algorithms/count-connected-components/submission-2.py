class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        # def dfs(node):
        #     for nei in adj[node]:
        #         if not visit[nei]:
        #             visit[nei] = True
        #             dfs(nei)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                # visit[node] = True
                # dfs(node)
                bfs(node)
                res += 1
        
        return res