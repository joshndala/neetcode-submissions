class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visited[node] = True

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True

        for node in range(n):
            if not visited[node]:
                bfs(node)
                result += 1

        return result