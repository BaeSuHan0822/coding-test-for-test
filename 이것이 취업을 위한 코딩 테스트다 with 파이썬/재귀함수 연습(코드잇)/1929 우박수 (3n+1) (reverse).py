import sys
sys.setrecursionlimit(10**6)

n = int(input())

def number(x) :
    if x == 1 :
        print(1)        # 종료조건
    elif x%2 == 0 :
        number(x//2)
        print(x)
    else :
        number(3*x + 1)
        print(x)

number(n)