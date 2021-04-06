
def encrypt(key, message):
    out_msg = ""
    for char in message:
        if char not in key:
            out_msg += char
            continue
​
        keyIndex = key.index(char)
        if keyIndex % 2 == 0:
            out_msg += key[keyIndex + 1]
        else:
            out_msg += key[keyIndex - 1]
    return out_msg

