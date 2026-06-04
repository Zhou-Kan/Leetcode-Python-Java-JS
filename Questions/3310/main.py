from collections import defaultdict
def remaining_methods(n: int, k: int, invocations: list[list[int]]) -> list[int]:
    # build a graph for invocations
    g = defaultdict(list)
    for u, v in invocations:
        g[u].append(v)

    # build a visited list for methods
    vis = [False] * n

    def dfs(i: int) -> None:
        if vis[i]:
            return  

        vis[i] = True

        for j in g[i]:
            if not vis[j]:
                dfs(j)
    
    # suspicious list
    dfs(k)
    suspicious = set(i for i in range(n) if vis[i])

    for u, v in invocations:
        if u not in suspicious and v in suspicious:
            return list(range(n))
        
    return [i for i in range(n) if i not in suspicious]

print(remaining_methods(5, 0, [[1,2],[0,2],[0,1],[3,4]]))
print(remaining_methods(4, 1, [[1,2],[0,1],[3,2]]))
print(remaining_methods(3, 2, [[1,2],[0,1],[2,0]]))

