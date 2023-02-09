n = int(input()) #컴퓨터의 수
m = int(input()) # 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1)
total = 0
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