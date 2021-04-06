
def ohms_law(v, r, i):
    lst1=[v, r, i]
    if lst1.count(None) != 1:
        return "Invalid"
    elif v == None:
        return round(r*i, 2)        
    elif r == None:
        return round(v/i, 2)
    elif i == None:
        return round(v/r, 2)

