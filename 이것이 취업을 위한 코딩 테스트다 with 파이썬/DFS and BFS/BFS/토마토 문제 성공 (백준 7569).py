import sys
from collections import deque
width,length,height = map(int,input().split())    
graph = [
    [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(length)] 
    for _ in range(height)]  

directions = [[0,0,1],[0,-1,0],[0,0,-1],[0,1,0],[1,0,0],[-1,0,0]]   #  탐색 방향 세팅

q = deque() 
days = 0
total_untomato = 0

for h in range(height) :                        # 다 익었는지 and 안 익은 토마토 찾아서 q에 넣기
    for l in range(length) :
        for w in range(width) :
            if graph[h][l][w] == 1 :            # 익은 토마토 q에 넣기
                q.append([h,l,w,0])                     
            elif graph[h][l][w] == 0 :
                total_untomato += 1             # 안 익은 토마토 개수 세기

if total_untomato == 0 :                        # 다 익었으면 프로그램 종료
    print(0)
    exit()                                      # exit() 함수 :  파이썬 프로그램 종료 명령어

while q :                                       # 안 익은 토마토 있으면 익히기 시작
    current = q.popleft()                       # 큐이기 때문에 popleft() + 시간 복잡도 줄이기
    for h,l,w in directions :
        next_h = current[0] + h
        next_l = current[1] + l
        next_w = current[2] + w
        days = current[3]

        if (-1<next_h<height and -1<next_l<length and -1<next_w<width     
            and graph[next_h][next_l][next_w] == 0 ) :       
            total_untomato -= 1                 # 안 익은 토마토 익히고 옆에 안 익힌 토마토랑 날짜 + 1 해서 q에 넣기
            graph[next_h][next_l][next_w] = 1   # 익힘 체크
            q.append([next_h,next_l,next_w,days+1])

if total_untomato != 0 :
    print(-1)
else :
    print(days)