N, X = map(int,input().split())
number = list(map(int,input().split()))
a = []
for n in number:
    if n < X :
        a.append(n)
print(*a)