
def dif_ciph(inpt):
    a=[]
    if type(inpt)==str:
        lst = [ord(inpt[0])]
        for i in range(len(inpt)):
            a.append(ord(inpt[i]))
        for i in range(1,len(a)):
            lst.append(a[i]-a[i-1])
        return lst
    else:
        lst=[inpt[0]]
        b=inpt[0]
        for i in range(1,len(inpt)):
            b+=inpt[i]
            lst.append(b)
        for i in lst:
            a.append(chr(i))
        final=''.join(a)
        return final

