import random

numbers  = list(range(1,46))

#로또 추첨 코드 작성
#random.sample/(population,k)
#Return a K length list
#the population sequence . 1~45 개 숫자 중
print(random.sample(numbers,6))

for i in range(5):
    lucky_numbers = random.sample(numbers,6)
    print(sorted(lucky_numbers))
