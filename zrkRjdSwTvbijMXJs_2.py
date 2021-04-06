
def encrypt(plncode, pad):
    myans = pad[0:5]
    for i in range(len(plncode)):
        myans += str((int(plncode[i])-int(pad[i+5]))%10)
    return myans
​
​
def decrypt(cypcode, pad):
    if cypcode[:5] != pad[:5]:
        return "Error: Key IDs don't match."
​
    myans = ''
    for i in range(5,len(cypcode)):
        myans += str((int(cypcode[i])+int(pad[i]))%10)
    return myans

