from collections import defaultdict, deque

def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    g = defaultdict(list)
    n = len(graph)

    for u, v in enumerate(graph):
        g[u].append(v)

    q = deque([0])
    vis = [False] * n

    while q:
    
        for _ in range(len(q)):
            node = q.popleft()
            print(node)
            vis[node] = True
            for v in g[node]:
                if not vis[v]:
                    q.append(v)

    return vis[-1]

print(all_paths_source_target([[1,2],[3],[3],[]]))