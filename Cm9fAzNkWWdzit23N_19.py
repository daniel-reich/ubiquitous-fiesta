
def wave(txt):
    if txt == ' ':
        return []
    elif len(txt) <= 1:
        return list(txt.upper())
    if txt[0] == ' ':
        ntxt = " Blue"
        lst = [ntxt]
        lst += helper(ntxt, 1) 
        return lst   
    else:  
        ntxt = txt[0].upper() + txt[1:]
        lst = [ntxt]
        lst += helper(ntxt, 0)
        return lst
​
​
def helper(txt, n):
    if n == len(txt) - 1:
        return []
    if txt[n+1] == ' ' and n + 2 >= len(txt) - 1:
        return []
    else:
        ntxt = txt[:n] + txt[n].lower() + txt[n+1].upper() + txt[n+2:]
        if txt[n+1] == ' ':
            return helper(ntxt, n+1)
        return [ntxt] + helper(ntxt, n+1)

