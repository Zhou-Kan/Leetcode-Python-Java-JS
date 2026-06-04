from collections import defaultdict, deque

def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    g = defaultdict(list)
    n = len(graph)

    for u, v in enumerate(graph):
        for i in v:
            g[u].append(i)

    vis = [False] * n 
    vis[0] = True
    ans = []

    def backtrack(start: int, path: list[int]) -> None:
        if start == n - 1:
            ans.append(path[:])
            return 
        
        for i in g[start]:
            if vis[i]:
                continue
                
            vis[i] = True
            path.append(i)
            backtrack(i, path)
            path.pop()
            vis[i] = False
    
    backtrack(0, [0])
    return ans
        


print(all_paths_source_target([[1,2],[3],[3],[]]))