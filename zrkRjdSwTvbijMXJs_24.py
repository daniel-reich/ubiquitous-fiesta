
def encrypt(plncode, pad):
    return pad[:5]+''.join(str((int(i)-int(pad[ind+5]))%10) for ind,i in enumerate(plncode))
​
def decrypt(plncode, pad):
    if plncode[:5]==pad[:5]:
        return ''.join(str((int(i)+int(pad[ind+5]))%10) for ind,i in enumerate(plncode[5:]))
    else: return "Error: Key IDs don't match."

