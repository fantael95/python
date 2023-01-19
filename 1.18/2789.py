text = list(map(str,input().upper()))
cnt=0
text2 = text[:]
text3 = ""
text1 = ['C','A','M','B','R','I','D','G','E']
for t in text :
    if t in text1 :
        text2.remove(text[cnt])
    cnt += 1
for i in text2:
    text3 = text3 + i
print(text3)