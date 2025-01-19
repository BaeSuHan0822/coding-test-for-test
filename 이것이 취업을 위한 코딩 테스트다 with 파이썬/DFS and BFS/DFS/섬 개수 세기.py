# 문제: 섬의 개수 세기 (DFS)

# 주어진 지도에서 '1'은 땅을, '0'은 바다를 의미한다.
# '1'로 연결된 모든 땅들을 하나의 섬으로 간주하고, 각 섬의 개수를 구하는 문제이다.
# 연결된 땅은 수평, 수직, 대각선 방향으로 연결된 땅을 포함한다.

# 입력:
# 첫째 줄에 두 정수 n, m (1 ≤ n, m ≤ 100)이 주어진다. n은 지도 세로 크기, m은 지도 가로 크기이다.
# 둘째 줄부터 n개의 줄에 걸쳐 m개의 정수로 이루어진 지도 정보가 주어진다. 
# 각 정수는 '0' 또는 '1'이다. '1'은 땅, '0'은 바다이다.

# 출력:
# 지도에서 섬의 개수를 출력한다.

# 예시 입력 1:
# 4 4
# 1 1 0 0
# 1 1 0 0
# 0 0 1 1
# 0 0 1 1

# 예시 출력 1:
# 2

# 예시 입력 2:
# 5 5
# 1 1 0 0 0
# 1 1 0 1 0
# 0 0 0 1 0
# 0 1 1 0 0
# 0 0 1 1 1

# 예시 출력 2:
# 3

# 예시 입력 3:
# 3 3
# 1 0 0
# 0 1 0
# 0 0 1

# 예시 출력 3:
# 1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
directions = [[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]
global total 
total = 0
stack = []

def dfs(a,b) :
        stack.append([a,b])
        visited[a][b] = True
        while stack :
            current = stack.pop()
            for row,col in directions :
                next_row = row + current[0]
                next_col = col + current[1]

                if (-1<next_row<n and -1<next_col<m
                    and graph[next_row][next_col] == 1
                    and not visited[next_row][next_col]) :

                    dfs(next_row,next_col)

for i in range(n) :
        for k in range(m) :
            if graph[i][k] == 1 and not visited[i][k] :
                total += 1
                dfs(i,k)

print(total)