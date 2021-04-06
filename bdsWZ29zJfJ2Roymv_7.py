
def swap_two(txt):
    s=''
    for i in range(0,len(txt),4):
        t=txt[i:i+4]
        if len(t)==4:
            s+=t[2:]+t[:2]
        else:
            s+=t
    return s

