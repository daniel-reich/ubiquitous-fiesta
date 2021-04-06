
def encrypt(plncode, pad):
    pad2 = pad[5:]
    arr = []
    for i in range(len(plncode)):
        arr.append(((int(plncode[i]) - int(pad2[i])) % 10))
    arr = [str(i) for i in arr]
    return pad[:5] + "".join(arr)
​
​
def decrypt(cypcode, pad):
    if cypcode[:5] != pad[:5]:
        return "Error: Key IDs don't match."
    cypcode2 = cypcode[5:]
    pad2 = pad[5:]
    arr = []
    for i in range(len(cypcode2)):
        arr.append((int(cypcode2[i]) + int(pad2[i])) % 10)
    arr = [str(i) for i in arr]
    return "".join(arr)

