
def grant_the_hint(txt):
    txtlst = txt.split()
    finalst = []
    sublst = []
    maxlength = max([len(word) for word in txtlst])
    for i in range(-1, maxlength):
        for txt in txtlst:
            if i == -1:
                sublst.append('_' * len(txt))
            else:
               sublst.append(txt[0:i+1] + ('_' * (len(txt)-(i+1))))
        finalst.append(" ".join(sublst))
        sublst = []
##        if i == 4:
##            break
    return finalst

