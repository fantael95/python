import sys
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))
d = list(map(int,sys.stdin.readline().split()))
f = list(map(int,sys.stdin.readline().split()))
e = [sum(a),sum(b),sum(c),sum(d),sum(f)]
print((e.index(max(e))+1) ,max(e))