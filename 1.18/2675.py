T = int(input())
A = ""
for t in range(1,T+1):
    a , b = map(str,input().split())
    b = list(str(b))
    a =int(a)
    for i in b:
        c = a * i
        c = str(c)
        A = A + c
    print(A)
    A = ""
