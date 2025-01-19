import sys
sys.setrecursionlimit(1000000)

n = int(input())
def number(x) :
    if x == 1 :
        return 1
    else :
        return x + number(x-1)

print(number(n))