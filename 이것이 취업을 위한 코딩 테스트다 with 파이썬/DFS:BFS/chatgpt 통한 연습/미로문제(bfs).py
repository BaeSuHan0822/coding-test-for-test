# 문제: 미로 탐색

# 문제 설명:
# 주어진 미로에서 (0, 0) 위치에서 (n-1, m-1) 위치로 이동하는 최단 경로를 구하는 문제입니다.
# 미로는 1과 0으로 이루어져 있으며, 1은 갈 수 있는 길을, 0은 벽을 의미합니다.
# 주어진 미로에서 시작점부터 끝점까지 최단 거리를 구하세요.
# 만약 도달할 수 없다면 -1을 출력합니다.

# 입력:
# 첫 번째 줄: n, m (n: 세로 크기, m: 가로 크기)
# 그 다음 n개의 줄: 각 줄마다 m개의 숫자(1 또는 0)가 주어짐

# 출력:
# (n-1, m-1)까지의 최단 거리를 출력하거나, 도달할 수 없으면 -1을 출력합니다.

# 예시 입력 1:
# 4 4
# 1 0 1 1
# 1 1 1 0
# 0 0 1 1
# 1 1 1 1

# 예시 출력 1:
# 7

# 예시 입력 2:
# 3 3
# 1 0 0
# 0 0 0
# 0 0 1

# 예시 출력 2:
# -1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  

def bfs(a,b) :
    q = []
    q.append([a,b])
    visited[a][b] = 1

    while q :
        current = q.pop(0)
        for row,col in directions :
            next_row = current[0]+row
            next_col = current[1]+col
            if (-1<next_row<n and -1<next_col<m) and graph[next_row][next_col] == 1:
                if visited[next_row][next_col] == 0 : 
                    q.append([next_row,next_col])
                    visited[next_row][next_col] = visited[current[0]][current[1]] + 1
                else :
                    continue
        if visited[n-1][m-1] != 0 :
            break
        
    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1

print(bfs(0,0))

