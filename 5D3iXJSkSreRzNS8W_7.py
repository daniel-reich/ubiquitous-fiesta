
def news_at_ten(txt, n):
    res =[ ]
    for i in range(n+1):res.append((' '*(n-i) + txt[0:i]).ljust(n,' '))
    for i in range(1,len(txt)+1):res.append(txt[i:i+n].ljust(n,' '))
    return res

