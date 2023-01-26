S = input()
number = list(map(str,S.split(","))) # 스플릿 ,로 구분
number = list(map(int,(number))) # 타입 정수로 변환
print(sum(number)) #합 출력