from collections import defaultdict
def min_score(n: int, roads: list[list[int]]) -> int:
    g = defaultdict(list)

    for u, v, s in roads:
        g[u].append((v, s))
        g[v].append((u, s))
    
    vis = [False] * n
    ans = float('inf')
    def dfs(i: int) -> None:
        nonlocal ans
        if vis[i]:
            return 
        vis[i] = True

        for j, k in g[i]:
            if not vis[j]:
                ans = min(ans, k)
                dfs(j)
    
    dfs(0)
    return ans

        
