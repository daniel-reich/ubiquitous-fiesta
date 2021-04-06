
def encrypt(key, message):
    groups = [key[i:i+2] for i in range(0, len(key) - 1, 2)]
    pairs = {}
​
    for a, b in groups:
        if a not in pairs:
            pairs[a] = b
        if b not in pairs:
            pairs[b] = a
​
    return ''.join(pairs.get(i, i) for i in message)

