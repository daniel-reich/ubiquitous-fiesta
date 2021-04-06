
def news_at_ten(txt,n):
    plist = []
    if n>len(txt):
        iters = n
    else:
        iters = len(txt)
    for i in range(iters+1):
        if len(txt[:i])<n:
            add = ((n-i)*' ' + txt[:i])
            if len(add)<n:
                add += (n-len(add))*' '
            plist.append(add)
        else:
            plist.append(txt[i-n:i])
    
    if len(txt)>n:
        iters = n
    else:
        iters = len(txt)
    
        
    plus = plist[-1]
    for i in range(1,iters+1):
        add = plus[i:]
        add += ' '*i
        plist.append(add)
    
    return plist

