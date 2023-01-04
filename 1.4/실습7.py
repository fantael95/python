number_list = [11, 2, 31, 4, -15, 11]

num_min=number_list[0]

for i in number_list:
    if num_min > i:
        num_min = i
print(num_min)
