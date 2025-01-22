computer = int(input())
n = int(input())
graph = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]
visited[1] = True
total = -1

for _ in range(n) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s) :
    visited[s] = True
    for i in graph[s] :
        if not visited[i] :
            dfs(i)

dfs(1)

for i in visited :
    if i :
        total += 1

print(total)