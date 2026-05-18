from collections import defaultdict
def find_circle_num(is_connected: list[list[int]]) -> int:
    g = defaultdict(list)
    n = len(is_connected)

    for i in range(n):
        for j in range(n):
            if is_connected[i][j]:
                g[i].append(j)
                g[j].append(i)

    visited = [False] * n

    def dfs(i: int) -> None:
        if visited[i]:
            return
        visited[i] = True
        for j in g[i]:
            if not visited[j]:
                dfs(j)
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    return ans

print(find_circle_num([[1,1,0],[1,1,0],[0,0,1]]))
