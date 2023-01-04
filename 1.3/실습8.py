a,b = map(int,input("입력 : ").split())

if a == b :
    print("False")
if a > b :
    for i in range(a,b-1,-1):
        if a == b :
            break
        count = 0
        print(i, end=(""))
if a < b :
    for i in range(b,a-1,-1):
        if a == b :
            break
        count = 0
        print(i, end=(""))

