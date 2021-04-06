
def encrypt(c, p, k='63719'):
    return k +''.join(str((int(d1) -int(d2))%10) for d1, d2 in zip(c, p[5:]))
​
def decrypt(c, p):
    if c[:5] != p[:5]: return "Error: Key IDs don't match."
    return ''.join(str((int(d1) +int(d2))%10) for d1, d2 in zip(c, p))[5:]

