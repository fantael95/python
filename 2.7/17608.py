import sys
N = int(sys.stdin.readline()) #막대기 갯수 입력
stick = [] # 막대기 길이를 저장할 빈 리스트 
height = 0 #높이를 비교하기 위해 변수 선언
cnt = 0 # 갯수를 세기 위해 변수 선언
for _ in range(N): # 막대기의 개수만큼 반복
    num = int(sys.stdin.readline()) # 각각 막대기의 높이 입력
    stick.append(num) # 막대기의 높이 리스트에 추가
for i in reversed(stick):
    if i > height:
        cnt += 1
        height = i
print(cnt)