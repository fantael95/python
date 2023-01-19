T = int(input())
a = []
for t in range(T):
    string = list(input().split())
    for i in string:
        a.append(i[::-1])
    print(*a)
    a = []

# 거꾸로 뒤에서 출력 하지만 단어 순서는 그대로 두고 단어 글자만 거꾸로 해야함


