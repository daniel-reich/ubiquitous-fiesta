
def plus_sign(txt):
    txt1=''
    if txt[0].isalpha() or txt[-1:].isalpha():
        return False
    else:
        for i in range(0,len(txt)):
            if txt[i].isalpha():
                if txt[i-1]=="+" and txt[i+1]=="+":
                    txt1+=txt[i]
            else:
                txt1+=txt[i]
    return txt1==txt

