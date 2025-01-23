n = int(input())
visited = [[False]*n for _ in range(n)]
graph = [list(map(int,input())) for _ in range(n)]
answer = []
directions = [[0,1],[-1,0],[0,-1],[1,0]]

from collections import deque

def bfs(a,b) :
    total_now = 1
    q = deque()
    q.append([a,b])
    visited[a][b] = True

    while q :
        current = q.popleft()

        for row,col in directions :
            next_row = row + current[0]
            next_col = col + current[1]

            if (-1<next_row<n and -1<next_col<n
                and graph[next_row][next_col] == 1
                and not visited[next_row][next_col]) :

                q.append([next_row,next_col])
                visited[next_row][next_col] = True
                total_now += 1
    
    answer.append(total_now)
    

for i in range(n) :
    for k in range(n) :
        if graph[i][k] == 1 and not visited[i][k] :
            bfs(i,k)

print(len(answer))
print(*sorted(answer),sep = '\n')