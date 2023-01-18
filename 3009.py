a , b = map(int,input().split())
c , d = map(int,input().split())
e , f = map(int,input().split())
A = [a, c, e]
B = [b, d, f]
C = (max(A)+min(A))*2 - a - c - e 
D = (max(B)+min(B))*2 - b - d - f
print(f'{C} {D}')
