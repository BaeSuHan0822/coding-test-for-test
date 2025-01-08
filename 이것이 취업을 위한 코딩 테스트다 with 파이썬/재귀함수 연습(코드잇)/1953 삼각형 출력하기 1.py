import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

def triangle(x) :
    if x == 1 :
        print('*')
    else :
        triangle(x-1)
        print('*' * x)

triangle(n)