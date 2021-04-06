
def digital_decipher(emessage, key):
    key = list((str(key) * (len(emessage) // len(str(key)) + 1))[:len(emessage)])
    return ''.join(chr(96-int(key[i])+emessage[i]) for i in range(len(key)))

