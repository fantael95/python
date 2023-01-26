# 어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.
score = input()
num = 0
for i in score:
    if i == 'A':
        num += 4
    elif i == 'B':
        num += 3
    elif i == 'C':
        num += 2
    elif i == 'D':
        num += 1
    if i == '+' :
        num += 0.3
    elif i == '0' :
        num += 0.0
    elif i == '-':
        num -= 0.3
    elif i == 'F':
        print(0.0)
        break
if num > 0:
    print(num)

dict_score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7}
print(dict_score.get(input(),0.0))