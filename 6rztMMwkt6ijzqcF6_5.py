
def is_repeated(strn):
    ism=""
    for i in strn:
        ism = ism+i
        ismhossz = len(ism)
        if ism == strn[ismhossz:ismhossz*2]:
            return (int((24/len(ism))))
    return False

