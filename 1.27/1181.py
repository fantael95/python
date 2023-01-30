N = int(input())
a = set()
for _ in range(N):
    word = input()
    a.add(word)
a = sorted(a)
a = sorted(a, key=len)
for i in a:
    print(i)