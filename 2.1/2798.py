from itertools import combinations
N , M = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
b = list(combinations(a,3))
c =[]
for i in b:
    if sum(i) <= M:
        c.append(sum(i))
if c: 
    print(max(c))