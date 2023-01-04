number1=int(input("미세먼지 농도를 입력하세요"))
if number1 < 30 :
    print("좋음")
elif number1 < 80 :
    print("보통")
elif number1 < 150:
    print("나쁨")
elif number1 > 151:
    print("매우나쁨")