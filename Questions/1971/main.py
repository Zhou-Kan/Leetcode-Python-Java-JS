from collections import defaultdict

def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    g = defaultdict

    for u, v in edges:
        g[u] = v
        g[v] = u

    vis = [False] * n

    def dfs(i: int) -> None:
        if vis[i]:
            return 
        
        vis[i] = True
        for j in g[i]:
            if not vis[j]:
                dfs(j)

    dfs(source)
    return vis[destination]