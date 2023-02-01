a = []
b = {}
for _ in range(10):
    num = int(input())
    a.append(num)
    if num in b :
        b[num] += 1
    else :
        b[num] =1
print(int(sum(a)/10)) 
print(max(b, key=b.get))