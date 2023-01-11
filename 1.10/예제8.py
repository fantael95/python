T = int(input("테스트케이스의 수를 입력하세요"))
list1=[]
list=[]
for i in range(1,T+1):
    list = map(int,input("%s번째 정수의 나열을 입력하세요(띄어쓰기로 구분)"%i).split())
    list1.append(list)

for j in list1:
    for k in j:
        print(k,end =" ")
    print()