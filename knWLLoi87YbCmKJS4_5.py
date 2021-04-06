
def happy(n):
    x=[]
    s=n
    while len(str(s))>1:
        a=0
        for i in range(len(str(s))):
            a+=int(str(s)[i])**2
        s=a
        x.append(s)
    return True if 1 in x else False

