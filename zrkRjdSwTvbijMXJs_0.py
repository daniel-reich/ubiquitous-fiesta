
def encrypt(plncode, pad):
    return pad[:5] + ''.join(str((int(a)-int(b))%10) for a, b in zip(plncode, pad[5:]))
    
def decrypt(cypcode, pad):
    if cypcode[:5] == pad[:5]:
        return ''.join(str((int(a)+int(b))%10) for a, b in zip(cypcode[5:], pad[5:]))
    return "Error: Key IDs don't match."

