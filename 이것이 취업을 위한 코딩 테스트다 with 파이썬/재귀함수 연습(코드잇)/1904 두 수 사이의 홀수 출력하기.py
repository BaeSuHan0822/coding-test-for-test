a,b = map(int,input().split())

def number(a,b) :
    if a == b :
        if a%2!=0 :
            print(a)
    else :
        if a%2!= 0 :
            print(a)
        number(a+1,b)

number(a,b)