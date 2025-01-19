n,m,k = map(int,input().split())
List = sorted(list(map(int,input().split())),reverse = True)
answer =[]
i = 0

while len(answer)!=m :
    if List[i] != List[i+1] and i == 0:
        for _ in range(k) :
            answer.append(List[i])
        answer.append(List[1])

    else :
        for _ in range(k*List.count(List[i])) :
            answer.append(List[i])
        
        i += 1*List.count(List[i])

print(sum(answer))