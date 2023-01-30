b = []
while True:
    a = input()
    b.append(a)
    if '고무오리 디버깅 시작' in b:
        b = []
    if '고무오리 디버깅 끝' in b :
        b.remove('고무오리 디버깅 끝')
        break
    if '고무오리' in b and '문제' not in b:
        b.append('문제')
        b.append('문제')
        b.remove('고무오리')
    if '고무오리' in b:
        b.remove('문제')
        b.remove('고무오리')
print('힝구') if  b else print('고무오리야 사랑해') 