string = input()
cnt = 0
happy = 0
sad = 0
for i in string:
    if i == ':' and cnt == 0:
        cnt += 1
    if i =='-' and cnt == 1 :
        cnt += 1
    if i == ')' and cnt ==2 :
        cnt += 1
    if i == '(' and cnt == 2:
        cnt = -1
    if cnt == 3:
        happy += 1
        cnt = 0
    if cnt == -1:
        sad += 1
        cnt = 0
if happy == 0 and sad == 0 :
    print('none')
elif happy == sad :
    print('unsure')
elif happy > sad :
    print('happy')
elif sad > happy :
    print('sad')