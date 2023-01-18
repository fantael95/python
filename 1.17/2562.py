a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
A = [a,b,c,d,e,f,g,h,i]
cnt = 0
num = 0
for i in A:
    num = num + 1    
    if i == max(A):
        print(i)
        print(num)
        break    
    if i > cnt :
        cnt = i