A, B = map(int,input().split())
for a in range(1,A+1):
    for _ in range(B):
        numbers = list(map(int,input().split()))
        print(*numbers)
        pass