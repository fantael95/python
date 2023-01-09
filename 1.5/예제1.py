dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 190000101
print(dict_variable["회사"]) # 하이퍼그로스

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) #  A
print(dict_variable["D"]) #  d
print(dict_variable["B"]) #  에러 b를 key인 B로 바꿔준다

dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000 2000+4000

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key]) 
#    "이름": "정우영",
#    "생년월일": "19000101",
#    "회사": "하이퍼그로스",

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False
print("이름" in dict_variable) # True

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 딕셔너리에 거주지가 없을 경우에 거주지 값을 서울특별시로 지정해준다

print(dict_variable) # 딕셔너리 내용 {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'} 

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    list_variable.append(3)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

#에러가 발생 리스트 내부에 3이 없기 때문입니다.

try:
    number = 1
    if number == 1:
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# if 문 뒤에 :이 생략되었기 때문입니다.

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100