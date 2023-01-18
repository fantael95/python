a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
A = [a, b, c, d, e]
cnt = 0
for i in A:
    if i < 40 :
        A[cnt] = 40
    cnt += 1   
print(int(sum(A)/5))