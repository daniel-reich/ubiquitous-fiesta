
def same_length(txt):
    oCache = 0
    zCache = 0
    charCache = None
    for i in txt:
        if i == '1':
            if charCache == '0':
                if oCache != zCache:
                    return False
                oCache = 0
                zCache = 0
            oCache +=1
            charCache = '1'
        elif i == '0':
            zCache += 1
            charCache = '0'
        else:
            return False
    if oCache == zCache:
        return True
    else:
        return False

