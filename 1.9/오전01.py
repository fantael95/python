mylist = ['서울', '서울' , '대전', '광주', '대전' ,'부산', '서울', '부산']
a = set()
for i in mylist:
    if i not in a:
        a.add(i)
print(a)