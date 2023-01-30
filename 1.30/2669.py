a = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            a[x][y]= 1
for i in a:
    cnt += i.count(1)
print(cnt)