string = input()
a = []
cnt = 0
b=[]
for i in string:
    cnt += 1
    b = string[(cnt*10)-10:10*cnt]
    if len(b) < 10:
        b = string[(cnt*10)-9:]
        print(b)
        break
    elif len(b) == 10:
        a.append(string[(cnt*10)-10:10*cnt])
        b = a
        print(*b)
    a=[]
    b=[]