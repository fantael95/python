a = input()
A = list(a)
cnt = 0
cnt1 = 0
cnt2 = 0
for i in A :
    if i  == '@':
        cnt +=1
    elif i == '(':
        cnt1 = cnt
        cnt = 0
print(cnt1,cnt)