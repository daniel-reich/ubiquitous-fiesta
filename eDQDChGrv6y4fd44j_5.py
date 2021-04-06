
def can_put(txt, dim):
    lst = txt.split() if txt.count(' ') else [txt]
    leng = [len(x) for x in lst]
    if dim[1] < max(leng) or dim[0] == 0:
        return False
    if dim[0] == 1:
        if dim[1] < len(txt):
            return False
    return True

