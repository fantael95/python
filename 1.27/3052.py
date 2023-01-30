c = set()
for _ in range(10):
    num = int(input())
    b = num%42
    c.add(b)
print(len(c))  