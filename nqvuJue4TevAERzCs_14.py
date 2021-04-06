
def has_digit(txt):
    M=[]
    for i in txt:
        if(i.isdigit()):
            M.append(True)
        else:
            M.append(False)
    return any([i==True for i in M])

