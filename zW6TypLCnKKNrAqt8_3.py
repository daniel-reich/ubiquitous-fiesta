
def left_side(ls):
    out = []
    for ix, i in enumerate(ls):
        ct = 0
        for j in ls[:ix]:
            ct = ct + (1 if j < i else 0)
        out.append(ct)
    return out
  
​
def right_side(ls):
    out = []
    ls.reverse()
    for ix, i in enumerate(ls):
        ct = 0
        for j in ls[:ix]:
            ct = ct + (1 if j < i else 0)
        out.append(ct)
    out.reverse()
    return out

