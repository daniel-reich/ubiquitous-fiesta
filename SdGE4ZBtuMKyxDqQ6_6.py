
def first_repeat(chars):
    l = sorted(list(chars))
    
    for ele in range(len(l)):
        if l[ele-1] == l[ele]:
            return l[ele]
    else :
        return '-1'

