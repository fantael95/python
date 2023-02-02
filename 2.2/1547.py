cups = {1: {'location' : 1,
                'ball' : 1 }, 
            2: {'location' : 2,
                'ball' : 0 },
            3: {'location' : 3,
                'ball' : 0 }}
for _ in range(int(input())):
    a, b = map(int,input().split())
    if cups[a]['ball'] == 1:
        cups[b]['ball'] = 1
        cups[a] ['ball']= 0
    elif cups[b]['ball'] == 1:
        cups[a]['ball'] = 1
        cups[b]['ball'] = 0
    cups[a]['location'] , cups[b]['location'] = cups[b]['location'], cups[a]['location']
if cups[1]['ball'] == 1:
    print(1)
if cups[2]['ball'] == 1:
    print(2)
if cups[3]['ball'] == 1:
    print(3)