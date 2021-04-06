
def censor_string(txt, lst, char):
    new=txt.split(" ")
    new_string=[]
    for word in new:
        for censor in lst:
            if word == censor:
                word=list(word)
                for n in range(len(word)):
                    word[n]=char
            word="".join(word)
        new_string.append(word)
    return " ".join(new_string)

