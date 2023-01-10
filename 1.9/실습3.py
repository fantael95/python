string =input("문자열을 입력하세요 : ") #사용자 입력
a=list(string)

for i in a:
    if 'e' in a:
        a.remove('e') 
result = ''.join(s for s in a)        
print(result)