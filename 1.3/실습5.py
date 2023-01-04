number=int(input())

if number > 100 or number < 0 :
    print("에러")
elif number >= 60:
    print("합격")
elif number <=60:
    print("불합격")
else :
    print("입력이 잘못되었습니다")

