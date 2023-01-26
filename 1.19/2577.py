a = {'0':1,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
num1 = int(input())
num2 = int(input())
num3 = int(input())
score = num1*num2*num3
score = str(score)
score = list(score)
for i in score:
    if i in a :
        a[i] += 1
    else :
        a[i] = 1
a = dict(sorted(a.items()))
for value in a.values():
    print(value)