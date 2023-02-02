word = input()
word_len = len(word)
list_word = []
for x in range(1, word_len-1):
    for y in range(x+1, word_len):
        a = word[:x]
        b = word[x:y]
        c = word[y:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        list_word.append(a+b+c)
print(sorted(list_word)[0])