
def unique_abbrev(abbs, words):
    for i in abbs:
        k = 0
        for j in words:
            if i == j[0:len(i)]: k+=1
        if k>1: return False
    return True

