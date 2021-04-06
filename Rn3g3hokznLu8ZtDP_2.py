
def increment_string(txt):
    if txt[-1].isdigit() == False:
        return txt+'1'
    a = ''
    b = 0
    for i in range(len(txt)):
        if txt[i].isdigit() == True:
            a = txt[:i]
            b = int(txt[i:])
            c = len(txt)-i
            break
    b += 1
​
    return a+str(b).zfill(c)

