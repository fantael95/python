num = int(input())
a = list(range(1,num+1))
b = []
while True:
    if len(a) == 1:
        b.append(a[0])
        print(*b)
        break

    elif len(a) > 2 :
        a.append(a[1])
        b.append(a[0])
        del a[0]
        del a[0]
    elif len(a) == 2 :
        b.append(a[0])
        del a[0]