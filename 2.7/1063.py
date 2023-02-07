x , y, N = input().split()
N = int(N)
location = {'R': (1, 0), 'L': (-1, 0), 'B': (0, 1), 'T': (0, -1), 'RT': (1, -1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (-1, 1)}
king_x , king_y = ord(x[0]) - 65, 8 - int(x[1])
stone_x , stone_y = ord(y[0]) - 65 , 8 - int(y[1])

for _ in range(N):
    t = input()
    king_nx , king_ny = king_x + location[t][0], king_y + location[t][1]
    if 0 <= king_nx < 8 and 0 <= king_ny < 8:
        if (king_nx,king_ny) ==  (stone_x,stone_y):
            stone_nx , stone_ny = stone_x + location[t][0], stone_y + location[t][1]
            if 0<= stone_nx <8 and 0 <= stone_ny < 8:
                stone_x , stone_y  = stone_nx, stone_ny
                king_x , king_y  = king_nx, king_ny
        else  :
                king_x, king_y = king_nx, king_ny

print(f'{chr(king_x+65)}{8- king_y}')
print(f'{chr(stone_x+65)}{8- stone_y}')