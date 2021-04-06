
def correct_sentences(s):
    words=s.split()
    for i in range(1,len(words)):
        if words[i].istitle():
            words[i-1]=words[i-1]+'.'
    r=words[0].capitalize()
    for i in range(1,len(words)):
        r=r+' '+words[i]
    r=r+'.'
    return r

