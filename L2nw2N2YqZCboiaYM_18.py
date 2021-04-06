
def repeated(s):
    if len(s) == 1:
        return False
    for i in range(len(s)//2,0,-1):
         if s.count(s[:i]) > 1 and s.count(s[:i])*len(s[:i]) ==  len(s):
                return True
    return False

