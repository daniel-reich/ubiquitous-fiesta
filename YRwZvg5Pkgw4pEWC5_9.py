
def flick_switch(lst):
    res = []
    v = True
    for i in lst:
        if i=='flick':v = not v
        res.append(v)
    return res

