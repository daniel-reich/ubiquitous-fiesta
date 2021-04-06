
def ohms_law(u, r, i):
    if u == None: 
        if r == None or i == None:
            return 'Invalid'
        else:
            return round(r*i,2)
    if r == None:
        if u == None or i == None:
            return 'Invalid'
        else:
            return round(u / i,2)
    if i == None:
        if u == None or r == None:
            return 'Invalid'
        else:
            return round(u / r,2)
    return 'Invalid'

