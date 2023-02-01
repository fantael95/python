a , b = map(int,input().split())
time = int(input())
b += time
if b >= 60:
    a += b//60
    b = b%60
if a >= 24:
    a -= 24
print(f'{a} {b}')