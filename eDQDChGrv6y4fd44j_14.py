
def can_put(txt, dim):
    a = []
    if dim[0] == 1:
        if len(txt) > dim[1]:
            return False
    txt = txt.split(' ')
    temp = txt[0]
​
    if len(temp) > dim[1]:
        return False
​
    for i in range(1,len(txt)):
        if len(temp + ' ' + txt[i]) > dim[1]:
            a.append(temp)
            temp = txt[i]
​
            if len(temp) > dim[1]:
                return False
        else:
            temp = temp + ' ' + txt[i]
​
    if len(a) > dim[0]:
        return False
​
    return True

