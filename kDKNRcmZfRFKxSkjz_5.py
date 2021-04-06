
def unmix(txt):  
    length = len(txt)
    return  ''.join([txt[i+1]+txt[0+i] for i in range(0,length-1,2)]) if length % 2 == 0 else   ''.join([txt[i+1]+txt[0+i] for i in range(0,length-1,2)])+txt[-1]

