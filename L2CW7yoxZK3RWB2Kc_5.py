
def encode(chunk, seq):
    ans = ""
    if len(chunk) < len(seq):
        chunk += " " * (len(seq) - len(chunk))
    return ''.join([chunk[s] for s in seq])
    
def nico_cipher(message, key):
    L = sorted([[key[i], i] for i in range(len(key))])
    seq = [el[1] for el in L]
    lk = len(key)
    k = 0
    encoded = ""
    while k * lk < len(message):
        chunk = message[k*lk:k*lk+lk]
        encoded += encode(chunk, seq)
        k += 1
    return encoded

