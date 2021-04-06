
def dif_ciph(inpt):
    if isinstance(inpt,str):
        return([ord(inpt[i])-ord(inpt[i-1]) if i>0 else ord(inpt[i]) \
                for i in range(len(inpt))])
    else:
        return(''.join([chr(sum(inpt[0:i+1])) for i in range(len(inpt))]))

