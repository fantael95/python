num1 = ['A','B','C']
num2 = ['D','E','F']
num3 = ['G','H','I']
num4 = ['J','K','L']
num5 = ['M','N','O']
num6 = ['P','Q','R','S']
num7 = ['T','U','V']
num8 = ['W','X','Y','Z']
num = 0
string = input()
for i in string:
    if i in num1 :
        num += 3
    if i in num2:
        num += 4
    if i in num3:
        num += 5
    if i in num4:
        num += 6
    if i in num5:
        num += 7
    if i in num6:
        num += 8
    if i in num7:
        num += 9
    if i in num8:
        num += 10
print(num)