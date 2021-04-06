
def secret_password(message):
    txt=message
    alph='abcdefghijklmnopqrstuvwxyz'
    if txt.isalpha()==False or len(txt)!=9:
        return "BANG! BANG! BANG!"
    for i in txt:
        if i.isupper():
            return "BANG! BANG! BANG!"
    else:
        a,b,c=txt[0:3],txt[3:6],txt[6::]
        a1=str((alph.index(a[0]))+1)
        a3=str((alph.index(a[2]))+1)
        A=a1+a[1]+a3
        B=b[::-1]
        c1=chr(ord(c[0])+1)
        c2=chr(ord(c[1])+1)
        c3=chr(ord(c[2])+1)
        C=c1+c2+c3
        return B+C+A

