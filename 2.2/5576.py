W_scroe = []
K_scroe = []
W = 0
K = 0
for _ in range(10):
    W_scroe.append(int(input()))
for _ in range(10):
    K_scroe.append(int(input()))
W_scroe.sort(reverse=True)
W = sum(list(W_scroe[0:3]))
K_scroe.sort(reverse=True)
K = sum(K_scroe[0:3])
print(f'{W} {K}')