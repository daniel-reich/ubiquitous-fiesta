
def is_isomorphic(s, t):
    c=''
    for i in range(len(s)):
        a=s[i];b=t[i]
        if s.count(a)!=t.count(b):
            return False
        if a not in c or b not in c:
            c+=a+b+chr(32)
        else:
            if a+b not in c and b+a not in c:
                return False
    return True

