# 상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
dict_a = {}
x = {}
n = int(input())
for _ in range(n):
    a , b = list(map(str,input().split()))
    dict_a[a] = b
for i in dict_a:
    if dict_a[i] == 'enter':
        x[i] = '1'
x = dict(sorted(x.items(), reverse=True))
for key in x.keys():
    print(key)