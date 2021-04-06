
def check(d1, d2, k):
    
    v1 = d1.get(k)
    v2 = d2.get(k)
    if v1 == v2:
        return True
    elif v1 != None and v2 != None and v1 != v2:
        return "Not the same"
    else:
        return "One's empty"

