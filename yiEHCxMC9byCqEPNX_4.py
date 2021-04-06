
import re
def is_palindrome(p):
    s = re.split('\s|,|!|\?|\'|\.|-', p)
    s = list(filter(None, s))
    normal=[]
    oppos=[]
    for i in s:
        for j in i:
            normal.append(j.lower())
    for i in s[::-1]:
        for j in i[::-1]:
            oppos.append(j.lower())        
    if "".join(normal)=="".join(oppos):
        return True
    else:
        return False

