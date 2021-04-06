
def comments_correct(txt):
    nlist = chunks(txt,2)
    for i in range(len(nlist)-1):
        if nlist[i] == "**":
            return False
        elif nlist[i] == "/*" and nlist[i+1] != "*/":
            return False
    else:
        if nlist[-1] == "*" or nlist[-1] == "/":
            return False
        else:
            return True
    
def chunks(l, n):
    flist = []
    for i in range(0, len(l), n):
        flist.append(l[i:i+n])
    return flist

