
def grant_the_hint(txt):
    words = txt.split()
    Hint = []
    for i in range(0,len(str(max(words, key=len)))+1):
        Sentence = ""
        for word in words:
            Sentence += word[:i].ljust(len(word),"_") + " "
        Hint.append(Sentence[:len(Sentence)-1])
    
    return Hint

