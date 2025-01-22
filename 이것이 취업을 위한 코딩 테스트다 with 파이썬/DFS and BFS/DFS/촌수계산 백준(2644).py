import sys
sys.setrecursionlimit(10**6)

people = int(input())
x,y = map(int,input().split())
n = int(input())
graph = [[] for _ in range(people+1)]
visited = [False for _ in range(people+1)]
for _ in range(n) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

total = 0

def dfs(a,b,total) :
    visited[a] = True
    if a == b :
        return total
    
    for i in graph[a] :
        if not visited[i] :
            result = dfs(i,b,total + 1)
            if result != -1 :
                return result
    
    return -1

print(dfs(x,y,total))