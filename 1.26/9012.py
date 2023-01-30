T = int(input())
for t in range(T):
    a = input()
    b = list(a)
    cnt = 0
    while True:
        if len(b)%2 == 1:
            print('NO')
            break
        if len(b) == 0 :
            print('YES')
            break
        if len(b) == 2 and b[0] == '(' and b[1] == ')':
            print("YES")
            break         
        if (cnt+1) >= len(b) :
            print("NO")
            break
        if b[cnt] == '(' and b[cnt+1] == ')':
            if len(b) > 2:
                del b[cnt]
                del b[cnt]
                cnt = -1
        cnt += 1
        if cnt > 50 :
            print('NO')
            break