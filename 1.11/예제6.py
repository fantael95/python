T = int(input()) 

for t in range(1, T+1):
    N = int(input()) 
    for _ in range(N):
        numbers = list(map(int,input().split()))
        print(*numbers)
        pass