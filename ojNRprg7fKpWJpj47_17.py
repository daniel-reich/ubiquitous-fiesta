
def shift_sentence(txt):
    x,y=[],''
    txt=txt.split()
    for word in txt:
        x.append(word[0])
    b=txt[0]
    c=x[-1]+b[1::]
    x1=x[0:-1]
    y+=c
    for word in txt[1::]:
        i=x.pop(0)
        d=i+word[1::]
        y+=' '+d        
    return y

