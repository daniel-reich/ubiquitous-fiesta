
def encrypt(key, message):
    mapping = {}
    for i in range(len(key) // 2):
        c1, c2 = key[2*i:2*i+2]
        if c1 not in mapping:
            mapping[c1] = c2
        if c2 not in mapping:
            mapping[c2] = c1
    return ''.join([mapping.get(c, c) for c in message])

