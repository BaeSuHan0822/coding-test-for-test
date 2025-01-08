n = int(input())

def number(x) :
    if x == 1 :
        print(1)
    else :
        number(x-1)
        print(x)
number(n)