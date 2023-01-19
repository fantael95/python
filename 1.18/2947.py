#동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.
number = list(map(int,input().split()))
numbers = [1,2,3,4,5]
cnt = 0
while True :
    if number == numbers:
        break
    elif number[cnt] > number[cnt+1]:
        number[cnt] , number[cnt+1] = number[cnt+1] , number[cnt]
        cnt += 1
        print(*number)
        cnt = 0
    elif number[cnt] < number[cnt+1]:
        cnt += 1



