fin = open("words.txt")
wordlst = []
for line in fin:
    word = line.strip()
    wordlst.append(word)

longword = [i for i in wordlst if len(i) > 20 ]
noe = [i for i in wordlst if 'e' not in i ]
print(longword)
print(len(noe))
print(len(wordlst))
