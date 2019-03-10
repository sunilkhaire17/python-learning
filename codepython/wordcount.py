l = "This is repeated repeated string string and your job is to count number of words in this sentence. This is repeated string and your job is to count number of words in this sentence."

wordlist = l.split(" ")
#print(wordlist)

worddict = {}

for word in wordlist:
    if word in worddict:
        worddict[word] = worddict[word]+1
    else:
        worddict[word]=1

print(worddict)