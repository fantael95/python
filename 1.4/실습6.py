number_list = [1, 2, 31, 4, -5, 11]

num_max=number_list[0]

for i in number_list:
    if num_max < i:
        num_max = i
print(num_max)
