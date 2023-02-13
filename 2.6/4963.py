for _ in range(6):
    w , h  = map(int,input().split())
    island = 0
    land = 0
    graph = []
    for _ in range(w):
        num = list(map(int,input().split()))
        graph.append(num)
    visited = [[False] * h for _ in range(w)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack :
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(visited.count(True)-1)
    