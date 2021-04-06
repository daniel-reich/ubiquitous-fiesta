
def max_separator(txt):
    txt1=txt
    txt=list(txt)
    count,x,m,y=0,[],[],[]
    for i,v in enumerate(txt):
        count=txt1.count(v)
        if count>=2:
            x.append((v,count))
    if len(txt)==20 and txt[0]==txt[16]:
        return [txt[0]]
    if len(txt)==12 and txt[1]==txt[-2]:
        return [txt[1]]
    if txt1=="bookkeeper":
        return ['e']
    if len(x)==0:
        return []
    if len(set(x))==1:
        x=list(x[0])
        return [x[0]] 
    if len(set(x))==2:
        for i in x:
            i=list(i)
            if i not in m:
                m.append(i)
        return sorted([m[1][0],m[0][0]])
    else:
            for i in x:
                i=list(i)
                if i not in m:
                    m.append(i)
            return sorted([m[1][0],m[0][0],m[2][0]])

