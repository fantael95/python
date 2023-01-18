T = int(input())
cnt = 0
c = list()
d = ['0','1','2','3','4','5','6','7','8','9']
for t in range(1,T+1):
    N = int(input())
    for i in range(1,9999):
        a = (i*N)
        b = list(str(a))
        for B in b:
            if B not in c :
                c.append(B)
                c.sort()
        if d == c :
            print(f'#{t} {a}')
            c = list()
            cnt = 0
            break