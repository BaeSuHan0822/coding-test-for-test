n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
visited[n-1][m-1] = float('inf')
directions = [[0,1],[-1,0],[0,-1],[1,0]]
def bfs(a,b) :
    q = []
    q.append([a,b])
    visited[a][b] = 1
    while q :
        current = q.pop(0)
        for row,col in directions :
            next_row = row + current[0]
            next_col = col + current[1]
            if (-1<next_row<n and -1<next_col<m
                and graph[next_row][next_col] == 1
                and visited[next_row][next_col] != 0 
                and visited[next_row][next_col] > visited[current[0]][current[1]] + 1):
                
                visited[next_row][next_col] = visited[current[0]][current[1]] + 1
            
            if (-1<next_row<n and -1<next_col<m
                and graph[next_row][next_col] == 1
                and visited[next_row][next_col] == 0) :

                q.append([next_row,next_col])
                visited[next_row][next_col] = visited[current[0]][current[1]] + 1
                
    return visited[n-1][m-1]

print(bfs(0,0))

# 성공했지만 조건문 반복 너무 많음
# 예시 돌렸을 때 bfs가 아닌 왠지 모르게 의도와 다르게 dfs로 만들어졌음
# chatgpt에게 코드 보여줬을 때 수정할 점 알려줌
'''
1. 중복 조건문 제거 
2. deque 사용
'''


# 수정코드

from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
directions = [[0,1],[-1,0],[0,-1],[1,0]]
def bfs(a,b) :
    q = deque()
    q.append([a,b])
    visited[a][b] = 1
    while q :
        current = q.popleft()
        for row,col in directions :
            next_row = row + current[0]
            next_col = col + current[1]
            
            if (-1<next_row<n and -1<next_col<m
                and graph[next_row][next_col] == 1
                and visited[next_row][next_col] == 0) :

                q.append([next_row,next_col])
                visited[next_row][next_col] = visited[current[0]][current[1]] + 1
                
    return visited[n-1][m-1]

print(bfs(0,0))