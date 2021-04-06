
f=lambda n:"A"[n:]or f(n-1)+chr(65+n)+f(n-1)
def ABA(s):
    s = ord(s)-65
    return f(s)

