
def syllabification(word):
​
    vo = ['A', 'a', 'e', 'i', 'o', 'u']  #1
    co = ['p', 'b', 't', 'd', 'c', 'J', 'G', '?', 'f', 'v', 's', 'z', 'F', '3', 'x', 'h', 'T', 'D', 'm', 'n', 'r', 'l', 'j'] #2
    a,b,d=[],[],[]    
    w= list(word)
    for i in w:
        if i in vo : a.append("1")            
        else: a.append("2")
    b="".join(a)  
    k=len(w)
    while k>0:       
        if b[-4:] == "2122":
            d.append("".join(w[-4:]))
            w,b = w[:-4], b[:-4]
        else:
            if b[-3:] == "212":
                d.append("".join(w[-3:]))
                w,b=w[:-3],b[:-3]
            else:
                if b[-2:] == "21":
                    d.append("".join(w[-2:]))
                    w,b=w[:-2],b[:-2]
        k=len(w)
​
    return ".".join(d[::-1])

