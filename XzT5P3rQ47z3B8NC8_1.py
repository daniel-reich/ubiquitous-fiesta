
def condi_cipher(message, key, shift):
    k, set_k = "", set()
    for c in key:
        if c not in set_k:
            k += c
            set_k.add(c)
    k += "".join(chr(i + 97) for i in range(26) if chr(i + 97) not in set_k)
    res = []
    for i, c in enumerate(message):
        if c.isalpha():
            x = k[(k.index(c) + shift) % 26]
            shift = k.index(c) + 1
        else:
            x = c
        res.append(x)
    return "".join(res)

