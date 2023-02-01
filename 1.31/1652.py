matrix = []
N = int(input())
for _ in range(N):
    matrix.append(list(input()))
cnt = 0 # 점 갯수
cnt1 = 0 # 자리 갯수
check = 1
b = ''
for i in matrix:
    cnt = 0
    check = 1
    for j in i:
        if j == '.':
            cnt += 1
        elif j == 'X':
            if cnt >= 2 :
                if check == 1:
                    cnt1 += 1
            cnt = 0
            check = 1
        if cnt >= 2:
            if check == 1:
                cnt1 += 1
                check = 0          
matrix_new = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix_new[i][j] = matrix[j][i]
cnt = 0
cnt2 = 0
for i in matrix_new:
    cnt = 0
    check = 1
    for j in i:
        if j == '.':
            cnt += 1
        elif j == 'X':
            if cnt >= 2 :
                if check == 1:
                    cnt2 += 1
            cnt = 0
            check = 1
        if cnt >= 2:
            if check == 1:
                cnt2 += 1
                check = 0    
print(f'{cnt1} {cnt2}')