
def simplify(txt):
    a, b = txt.split("/")
    a = int(a)
    b = int(b)
    
    t = ggT(a,b)
    a = a//t
    b = b//t
    
    if b!=1:
        return str(a)+ "/" +str(b)
    else:
        return str(a)
    
    
def ggT(a, b):
    if b == 0:
        return a
    return ggT(b, a%b)

