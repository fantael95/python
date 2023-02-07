N = int(input()) #막대기 갯수 입력
stick = [] # 막대기 길이를 저장할 빈 리스트 
height = 0 #높이를 비교하기 위해 변수 선언
cnt = 0 # 갯수를 세기 위해 변수 선언
for _ in range(N): # 막대기의 개수만큼 반복
    num = int(input()) # 각각 막대기의 높이 입력
    if not stick : # 리스트가 비어있을 경우
        stick.append(num) # 막대기의 높이 리스트에 추가
    if num > max(stick): #입력한 숫자가 리스트의 최대숫자보다 높을 경우
        stick = [] #리스트를 지우고
        stick.append(num) # 입력한 숫자만 채운다
    if num < max(stick) : # 입력한 숫자가 최대 숫자보단 작을 경우 
        if num < min(stick) : # 최소 숫자보다 작으면
            stick.append(num) # 리스트에 추가
        elif num > min(stick) :
            while num > min(stick):
                stick.remove(min(stick))
            if num not in stick:
                stick.append(num)
print(len(stick))
