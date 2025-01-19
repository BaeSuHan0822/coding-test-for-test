# 문제: 미로에서 출구 찾기 (DFS)
#
# 문제 설명:
# n x n 크기의 미로가 주어진다. 0은 이동 가능한 길이고, 1은 이동할 수 없는 벽이다.
# (0, 0)에서 출발하여 (n-1, n-1)까지 도달할 수 있는지 확인하는 프로그램을 작성하라.
# 도달할 수 있으면 "Yes", 도달할 수 없으면 "No"를 출력한다.
#
# 입력 형식:
# 1. 첫 번째 줄에 정수 n(미로의 크기)이 주어진다. (2 <= n <= 100)
# 2. 다음 n개의 줄에 걸쳐 0과 1로 이루어진 n개의 숫자가 주어진다.
#    각 숫자는 공백으로 구분된다.
#
# 출력 형식:
# 도달 가능하면 "Yes", 불가능하면 "No"를 출력한다.
#
# 입력 예시:
# 5
# 0 1 0 0 0
# 0 1 0 1 0
# 0 0 0 1 0
# 1 1 1 1 0
# 0 0 0 0 0
#
# 출력 예시:
# Yes
#
# 입력 설명:
# 미로의 크기는 5x5이고, (0, 0)에서 출발해 (4, 4)로 이동할 수 있는 경로가 있다.

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
directions = [[0,1],[-1,0],[0,-1],[1,0]]
visited = [[False]*n for _ in range(n)]
def dfs(a,b) :
    stack = []
    stack.append([a,b])
    visited[a][b] = True

    while stack :
        current = stack.pop()
        if current[0] == n-1 and current[1] == n-1 :
            return "Yes"
        
        for row,col in directions :
            next_row = row + current[0]
            next_col = col + current[1]

            if (-1<next_row<n and -1<next_col<n 
                and graph[next_row][next_col] == 0
                and not visited[next_row][next_col] ) :
                stack.append([next_row,next_col])
                visited[next_row][next_col] = True
            
    return "No"

print(dfs(0,0))