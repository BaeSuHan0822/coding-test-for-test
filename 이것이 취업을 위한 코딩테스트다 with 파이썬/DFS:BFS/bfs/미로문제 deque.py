n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
directions = [[0,1],[-1,0],[0,-1],[1,0]]

from collections import deque

def bfs(a,b) :
    q = deque()         #deque 사용
    q.append([a,b])
    visited[a][b] = 1

    while q :
        current = q.popleft()

        if current[0] == n-1 and current[1] == m-1 :
            return visited[n-1][m-1]
        
        for row,col in directions :
            next_row = row + current[0]
            next_col = col + current[1]

            if (-1<next_row<n and -1<next_col<m 
                and graph[next_row][next_col] == 1
                and visited[next_row][next_col] == 0) :
                
                    q.append([next_row,next_col])
                    visited[next_row][next_col] = visited[current[0]][current[1]] + 1
        
    return -1

print(bfs(0,0))