import sys
sys.setrecursionlimit(10**6)

n = int(input())
dp = [0] * 201
dp[1] = 1
dp[2] = 1

def fib(x) :
    if dp[x] == 1 :       # 종료 조건
        return 1 
    elif dp[x] != 0 :       #dp 결과 저장값 이용
        return dp[x]
    else :             # dp 결과값 아직 없을 때 
        fib(x-1)
        dp[x] = dp[x-1]+ dp[x-2]
        return dp[x]


print(fib(n)%10009)