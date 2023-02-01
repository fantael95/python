matrix = []
num = []
matrix_new = []
for _ in range(5):
    a = list(input())
    num.append(len(a))
    c = max(num)
    matrix.append(a)
for i in matrix:
    if len(i) < c :
        i = i + (c-len(i))*[0]
        matrix_new.append(i)
    else:
        matrix_new.append(i)
transposed_matrix = [[0]*15 for _ in range(15)]
for i in range(c):
    for j in range(5):
        transposed_matrix[i][j] = matrix_new[j][i]
b = ''
for i in transposed_matrix:
    for k in i:
        if k != 0:
            b += k
b = b.replace(" ","")
print(b)