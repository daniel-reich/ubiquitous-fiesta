
def mirror_cipher(message, key="abcdefghijklmnopqrstuvwxyz"):
    key = key.lower()
    n = len(key)
    encoded = ""
    for c in message.lower():
        if c in key:
            encoded += key[n - 1 - key.index(c)]
        else:
            encoded += c
    return encoded

