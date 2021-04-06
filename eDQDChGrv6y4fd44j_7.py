
def can_put(txt, dim):
    t=txt.split()
    i=s=k=0
    while i<len(t):
        s+=len(t[i])+(s>0)
        if s>dim[1]:
            k+=1
            s=0
        else:
            i+=1
        if k>=dim[0]:
            return False
    return True

