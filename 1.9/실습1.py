string = input("문자열을 입력하세요 : ") #사용자 입력
cnt=0
for i in string:
    if 'e' not in string:
        print('-1')
        break
    elif 'e' in string:
        cnt += 1
print(cnt-1)