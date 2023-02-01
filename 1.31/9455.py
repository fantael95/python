for _ in range(int(input())):
    a, b = map(int,input().split())
    matrix = []
    for _ in range(a):
        num = list(input().split())
        matrix.append(num)
    matrix_new = [[0]*a for _ in range(b)]
    for i in range(b):
        for j in range(a):
            matrix_new[i][j] = matrix[a-j-1][i]
    number = 0
    for i in matrix_new:
            height = 0
            black =0
            for k in i:
                if height == len(i):
                        height = 0
                elif height == 0:
                    if k == '0':
                        height += 1
                    elif k == '1':
                        height += 1
                        black += 1 
                else :
                    if k == '1':
                        number += (height - black)
                        black += 1
                        height +=1
                    elif k == '0':
                        height +=1   
    print(number)
    number = 0