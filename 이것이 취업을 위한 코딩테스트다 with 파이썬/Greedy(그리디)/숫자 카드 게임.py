# 내 정답
m,n = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(m)]

answer = float("-inf")
for i in range(m) :
    if answer < min(data[i]) :
        answer = min(data[i])

print(answer)


# 풀이
#1. min() 함수 사용
n,m = map(int,input().split())

result = 0
for i in range(n) :
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(min_value,result)

print(result)


#2. 2중 반복문 구조를 이용
n,m = map(int,input().split())

result = 0

for i in range(n) :
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data :
        min_value = min(min_value,a)

    result = max(result,min_value)

print(result)