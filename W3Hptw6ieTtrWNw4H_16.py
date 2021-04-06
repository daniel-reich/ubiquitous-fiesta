
def encipher1(text,T):
    text="".join([e for e in text if e.isalpha()])
    text=text.upper()
    A="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    d={"J":"24"}
    b=""
    s=['A']*(2*len(text))
    for i in range(5):
        for j in range(5):
            d[A[5*i+j]]=str(i+1)+str(j+1)
    d1={b:a for a,b in d.items() if a!="J"}
    for i in text:
        b+=d[i]
    s1=""
​
    if T:
        for i in range(0,len(b),2):
            s[i//2]=b[i]
            s[len(text)+i//2]=b[i+1]
        a="".join(s)
        for i in range(0,len(a),2):
            s1+=d1[a[i:i+2]]
    else :
        for i in range(0,len(text)):
            s[2*i]=b[i]
        for i in range(0,len(text)):
            s[2*i+1]=b[len(text)+i]
        a="".join(s)
        for i in range(0,len(a),2):
            s1+=d1[a[i:i+2]]
    return s1.lower()
​
def bifid(text):
    T=True
    j=text.find(" ")
    if j==-1:
        T=False
    return encipher1(text,T)

