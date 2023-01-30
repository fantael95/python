import sys
N = int(sys.stdin.readline())
a = ''
for _ in range(1,N+1):
    a += f"{'*'*_}\n"
print(a)