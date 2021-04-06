
def mirror_cipher(msg, k="abcdefghijklmnopqrstuvwxyz"):
    len_k_1 = len(k) - 1
    return "".join(k[len_k_1 - k.index(c)] if c in k else c
                   for c in msg.lower())

