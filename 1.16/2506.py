N = int(input())
A = list(map(int,input().split()))
score = 0 
num = 0
for a in A:
    if a == 0 :
        num = 0
    else :
        num +=  1
        score += num
print(score)