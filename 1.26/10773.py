K = int(input())
a = []
cnt = 0
for i in range(K):
    i = int(input())
    if i == 0:
        a.pop(cnt-1)
        cnt -= 1
    else :
        a.append(i)
        cnt += 1
print(sum(a))
