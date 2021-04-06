
def keyword_cipher(key, message):
    keystr = ""
    for k in key:
        if k not in keystr:
            keystr += k
    for k in range(97, 123):
        c = chr(k)
        if c not in keystr:
            keystr += c
    enc = ""
    for m in message:
        if 'a' <= m <= 'z':
            idx = ord(m) - 97
            enc += keystr[idx]
        else:
            enc += m
    return enc

