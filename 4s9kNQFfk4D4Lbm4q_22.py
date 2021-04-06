
def ABA(s):
    if ord(s) == 65: return s
    else:
        return ABA(chr(ord(s)-1))+s+ABA(chr(ord(s)-1))

