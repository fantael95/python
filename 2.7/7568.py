N = int(input()) # 사람의 수 N 입력
body = [] #리스트
body_num = []
cnt = 1
for _ in range(N): #사람의 수만큼 입력 반복
    x, y = map(int,input().split()) # 체중, 키 입력
    body.append([x,y]) # 리스트에 추가
for i in body:
    for j in body:
        if i != j :
            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1
    body_num.append(cnt)
    cnt = 1
print(*body_num)