road = []
road_len = []
N = int(input())
a = list(map(int,input().split()))
for _ in range(N-1):
    if a[_] < a[_+1] :
        if a[_] not in road:
            road.append(a[_])
        if a[_+1] not in road:
            road.append(a[_+1])
    else :
        if road :
            road_len.append(max(road) - min(road))
            road = []
if road :
    road_len.append(max(road) - min(road))
if road_len:
    print(max(road_len))
else :
    print(0)