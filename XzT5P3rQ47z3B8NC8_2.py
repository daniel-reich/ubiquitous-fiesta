
def condi_cipher(message, key, shift):
    # step 1:
    Key = []
    for k in key:
        if k not in Key:
            Key.append(k)
    key = Key
    for i in range(97, 123):
        c = chr(i)
        if c not in key:
            key.append(c)
    # steps 2-4:
    cipher = ""
    for c in message:
        if c.isalpha():
            idx = key.index(c)
            cipher += key[(idx + shift) % 26]
            shift = idx + 1
        else:
            cipher += c
    return cipher

