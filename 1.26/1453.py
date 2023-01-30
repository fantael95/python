N = int(input())
cnt = 0
a = {}
if N > 100 :
    print('Error')
num = list(map(int,input().split()))
for i in num:
    if i in a :
        cnt += 1
    if i not in a :
        a[i] = 1
print(cnt)

