import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0 and not heap :
        print('0')
    elif x == 0 :
        print(heapq.heappop(heap))
    else :
        heapq.heappush(heap, x)