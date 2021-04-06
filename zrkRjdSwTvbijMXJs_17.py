
def encrypt(plncode, pad):
    cyp = [(int(plncode[x])-int(y))%10 for x,y in enumerate(pad[5:len(plncode)+5])]
    return pad[:5]+''.join(map(str,cyp))
​
def decrypt(cypcode, pad):
    if not cypcode[:5] == pad[:5]:
        return "Error: Key IDs don't match."
    pln = [(int(cypcode[x])+int(y))%10 for x,y in enumerate(pad[:len(cypcode)])]
    return ''.join(map(str,pln[5:]))

