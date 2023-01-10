string = list(input("문자열을 입력하세요 : ").split()) #사용자 입력
word = dict()

for i in string:
    if i not in word:
        word[i]=0
    if i in word:
        word[i] +=1

for key, value in word.items():
    print(f'{key}{value}')