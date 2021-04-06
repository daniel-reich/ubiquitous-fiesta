
def abcmath(a, b, c):
    s=b
    f=a
    while s>0:
        l=f+f
        f=l
        s=s-1
    if l%c==0:
        return True
    else:
        return False

