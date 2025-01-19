import sys
sys.setrecursionlimit(10**6)

n = int(input())

def number(x) :
    if x == 1 :
        print(1)         # 종료조건
    elif x%2 == 0 :
        print(x)
        number(x//2)
    else :
        print(x)
        number(3*x + 1)

number(n)