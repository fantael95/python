ride = 0
max_ride = 0
for _ in range(1,5):
    a, b = map(int,input().split())
    ride += b
    ride -= a
    if ride > max_ride:
        max_ride = ride
print(max_ride)