N = int(input())
a = []
for n in range(1,N+1):
    number = int(input())
    if number in a :
        pass
    else : 
        a.append(number)
    if len(a) == N:
        a.sort()
        for k in a:
            print(k)
    
