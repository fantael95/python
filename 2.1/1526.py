N = int(input())
num = list(range(4,N+1))
num_list = []
for i in num :
    a = list(str(i))
    cnt = 0
    for j in a:
        if j == '4' :
            cnt += 1
            if cnt == len(a):
                num_list.append(i)
        elif j == '7' :
            cnt += 1
            if cnt == len(a):
                num_list.append(i)
if num_list :
    print(max(num_list))