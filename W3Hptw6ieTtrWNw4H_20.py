
def bifid(text):
    ctp=" " in text
    text=text.lower()
    text=text.replace("j","i")
    ltx=[]
    for x in text:
        if x.isalpha():
            ltx.append(x)
    text=''.join(ltx)
​
    tbook={"a":[1,1],"b":[1,2],"c":[1,3],"d":[1,4],"e":[1,5],
    "f":[2,1],"g":[2,2],"h":[2,3],"i":[2,4],"k":[2,5],
    "l":[3,1],"m":[3,2],"n":[3,3],"o":[3,4],"p":[3,5],
    "q":[4,1],"r":[4,2],"s":[4,3],"t":[4,4],"u":[4,5],
    "v":[5,1],"w":[5,2],"x":[5,3],"y":[5,4],"z":[5,5]}
    
    if ctp :
        l1=[];l2=[]
        for a in text:
            l1.append(tbook[a][0])
            l2.append(tbook[a][1])
        lx=l1+l2
        lx1=lx[0:-1:2]
        lx2=lx[1::2]
    else:
        ltext=[]
        for a in text:
            ltext=ltext+tbook[a]
        lx1=ltext[:len(text)]
        lx2=ltext[len(text):]
    
    lc=[]  
    for i in range(len(text)):
        x=list(tbook.values()).index([lx1[i],lx2[i]])
        lc.append(list(tbook.keys())[x])    
    ctext="".join(lc)
    return ctext

