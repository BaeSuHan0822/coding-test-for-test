n = int(input())

def number(x) :
    if x == 1 :
        print(1)
    else :
        print(x)
        number(x-1)

number(n)
