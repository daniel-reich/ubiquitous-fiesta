
def deep_sum(lst):
    a,b,c,rr=[],[],[],[]
    num="0123456789"
    for t in range(20): 
        for i in lst:
            if type(i)==list:
                for j in i:b.append(j)
            else:b.append(i)  
        if lst==b : break
        else:lst=b
        b=[]
    for i in b:
        e=[]
        if not len(i)==0:
            if i[0]=='-':
                if len(i)>0:
                    e=list(i)
                    for k in range(1,len(i)):
                        if not i[k] in num:
                            e.remove(i[k])
                            if i[k]=='-': 
                                b.append("".join(i[k:]))
                            elif not i[k] in num:
                                b.append("".join(i[k+1:]))
                            c.append("".join(i[0:k]))
                            break
                if e==list(i) :
                    c.append("".join(e))
            elif not (i[0] in num or i[0]=='-'):
                b.append(i[1:])
            else:
                e=list(i)
                for k in range(0,len(i)):
                    if not i[k] in num:
                        e.remove(i[k])
                        if i[k]=='-': 
                            b.append("".join(i[k:]))
                        elif not i[k] in num:
                            b.append("".join(i[k+1:]))
                        c.append("".join(i[0:k]))
                        break
                if e==list(i) :
                    c.append("".join(e))
    for i in c:
        if not (i=='' or i=="-"):rr.append(int(i))    
    return (sum(rr))

