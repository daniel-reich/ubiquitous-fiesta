
def encrypt(key, message):
    d = dict()
    for i, c in enumerate(key):
        if c not in d:
            if i % 2:
                d[c] = key[i - 1]
            else:
                d[c] = key[i + 1]
    return "".join(d[c] if c in d else c for c in message)

