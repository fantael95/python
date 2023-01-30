import sys
a, b = map(str,sys.stdin.readline().split()) # a , b 정수형으로 입력받기
sum_num = 0 # 합을 구할 변수 선언
number = 0
c = list(map(int,a)) #리스트 자료형 정수로 변환
d = list(map(int,b))
e = sum(d) # 하나씩 곱하고 더하는 것을 간소화해 b를 전부 더한다 ((1*2) +(1*1) = (1*3))
for i in c: 
    number += e*i
print(number)
