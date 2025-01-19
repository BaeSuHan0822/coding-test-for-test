import sys
sys.setrecursionlimit(10**6)
answer = []
dp = [[e for e in range(15)]]
dp = dp + [[0]*15 for _ in range(14)]


def superSum(a,b) :
    if a == 0  :        #종료조건
        return dp[a][b]
    elif dp[a][b] != 0 :
        return dp[a][b]
    else :             #기본동작
        result = 0
        for i in range(1,b+1) :
            result += superSum(a-1,i)
        dp[a][b] = result
        return result

while True :
    try :
        k,n = map(int,sys.stdin.readline().rstrip().split())
        answer.append(superSum(k,n))
    except EOFError :
        print(*answer,sep = '\n')
        break