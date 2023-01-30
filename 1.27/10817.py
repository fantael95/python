A, B, C = map(int,input().split())
cnt = 0
b = [A, B, C]
for i in b:
    if i == max(b):
        b.remove(max(b))
        print(max(b))
        break

    
