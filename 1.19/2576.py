#7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
A = [a,b,c,d,e,f,g]
B = list()
c = {}
for i in A:
    if i%2==1 :
        B.append(i)
        c[i]=1
if len(B) == 0:
    print(-1)
elif len(B) != 0:
    print(sum(B))
    print(min(B))