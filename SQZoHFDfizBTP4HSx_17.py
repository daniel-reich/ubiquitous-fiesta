
def missing_alphabets(txt):
    x="abcdefghijklmnopqrstuvwxyz"
    res=''
    if len(x)==len(txt):
        return ""
    b=txt.count(txt[1])
    if b==1:
        for i in x:
            if i not in txt:
                res+=i
        return res        
    else:
        rs=''
        for i in x:
            c=txt.count(i)
            if c>1 and i not in rs:
                rs+=i*c
            else:
                res+=i*c
                if i not in res:
                    res+=i*b
        return res

