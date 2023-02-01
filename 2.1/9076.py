T = int(input())
for _ in range(T):
    score = list(map(int,input().split()))
    Max_check = 1
    Min_Check = 1
    for i in score:
        if i == max(score) and Max_check == 1:
            score.remove(i)
            Max_check = 0
        elif i == min(score) and Min_Check == 1:
            score.remove(i)
            Min_Check = 0
    if (max(score)-min(score)) >= 4 : 
        print('KIN')
    else :
        print(sum(score))