letter=dict()
string=input("문자열을 입력하세요")

for i in string :
    if i in letter :
        letter[i] += 1
    else:
        letter[i] = 1
for key, value in letter.items():
    print(key,value)