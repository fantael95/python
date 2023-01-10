numbers=input("숫자를 입력하세요 : ")
b=int(numbers)
if b < 0 :
    print('-1')
else : 
    a=list(map(int,(numbers)))
    cnt=0
    for i in a:
        if i < 0:
           print('-1')
           break
        else :
            cnt += i
    print(cnt)        
