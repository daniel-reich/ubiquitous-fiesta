
def reverse_words(words):
    words=words.split()
    leWords=len(words)
    print(leWords)
    ausg=['']*leWords
    i=0
    while i<leWords:
        ausg[i]=words[leWords-i-1]
        i+=1
    ausg=' '.join(ausg)
    return ausg

