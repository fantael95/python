#1
N = int(input())
new_a = []
for _ in range(N,0,-1):
    new_a.append((" "*(N-_)) + ('*'*_))
print(*new_a, sep='\n')

#2
a = []
rev_a = []
for _ in range(N,0,-1):
    a.append([('*'*_)+(" "*(N-_))])
for _ in range(N):
        rev_a[_] = a[_-1]
print(rev_a)
