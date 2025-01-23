import sys
width,length,h = map(int,input().split()) # n =
graph = [[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(length)] for _ in range(h)]
visited = [[[0 for _ in range(width)] for _ in range(length)] for _ in range(h)]
directions = [[0,0,1],[0,-1,0],[0,0,-1],[0,1,0],[1,0,0],[-1,0,0]]
answer = [0]
from collections import deque

def bfs(x,y,z) :
    q = deque()
    q.append([x,y,z])
    visited[x][y][z] = 1

    while q :
        current = q.popleft()
        for height,row,col in directions :
            next_height = height + current[0]
            next_row = row + current[1]
            next_col = col + current[2]
            
            if (-1<next_height<h and -1<next_row<length and -1<next_col<width
                and graph[next_height][next_row][next_col] == 0
                and visited[next_height][next_row][next_col] == 0) :

                q.append([next_height,next_row,next_col])
                visited[next_height][next_row][next_col] = visited[current[0]][current[1]][current[2]] + 1

                if visited[next_height][next_row][next_col] not in answer :
                    answer.append(visited[next_height][next_row][next_col])
            
            if (-1<next_height<h and -1<next_row<length and -1<next_col<width and graph[next_height][next_row][next_col] == -1) or (-1<next_height<h and -1<next_row<length and -1<next_col<width and graph[next_height][next_row][next_col]) == 1 :
                
                visited[next_height][next_row][next_col] = visited[current[0]][current[1]][current[2]] + 1

for a in range(h) :
    for b in range(length) :
        for c in range(width) :
            if visited[a][b][c] == 0  and graph[a][b][c] == 1:
                bfs(a,b,c)


'''
문제점
1. 처음부터 다 익힌 토마토가 들어올 때 (익힐 토마토가 없을때) 처리 방법 없음
2. graph에서 1과 -1을 처리할 방법 없음 
    -> 다른 숫자로 대체 할려고 했으나 그러면 옆에 있는 값들에 영향 끼침
3. 만약 다 익힐 수 있다면 최종 날짜를 출력하기에 또 다시 answer라는 배열을 돌아야 함

해결 방법
처음에 graph를 돌면서 큐에 안 익은 토마토 넣어서 익은 토마토 위치에서 전부 시작하기
    -> 전부 다 익었다면 그대로 프로그램 종료
    -> 불필요한 조건 삭제 가능
'''
