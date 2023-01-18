T = int(input())
cnt= 0
for t in range(1,T+1):
    a = list(map(int,input().split()))
    for k in a :
        if k%2 == 1 :
            cnt = cnt + k
    print(f'#{t} {cnt}')
    cnt = 0