word = input()
word1 = list(word)
word2 = word1[:]
word1.reverse()
if word1 == word2:
    print('1')
else:
    print('0')