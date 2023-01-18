cnt = 0
num = int(input())
a = num 
while True:
    x , y = num//10, num%10
    num = y*10 + (x+y)%10
    cnt += 1
    if num == a:
        break
print(cnt)