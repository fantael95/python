a , b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
cnt = 0
c = (A-B)
d = (B-A)
e = len(c)+len(d)
print(e)