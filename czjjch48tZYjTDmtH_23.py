
def is_shifted(l1,l2):
    s=set()
    zp=list(zip(l1,l2))
    for a,b in zp:
        s.add((b-a))
    if len(s)==1:
        return True
    return False
  
def is_multiplied(l1,l2):
    s=set()
    zp=list(zip(l1,l2))
    for a,b in zp:
        s.add((b/a))
    if len(s)==1:
        return True
    return False

