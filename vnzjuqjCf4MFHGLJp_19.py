
def shift_letters(txt, n):
    l=len(txt)
    sp=[i for i in range(len(txt)) if txt[i]==' ']
    txt=txt.replace(' ','')
    for i in range(n):
        txt=txt[-1]+txt[:-1]
    for i in range(l):
        if i in sp:
            txt=txt[:i]+' '+txt[i:]
    return txt

