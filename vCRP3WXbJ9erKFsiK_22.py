
def dif_ciph(inpt):    
    result = []
    acc = 0
    if isinstance(inpt, str):
        for char in inpt:
            result.append(ord(char) - acc)
            acc = ord(char)
        return result
    for num in inpt:
        acc = num + acc
        result.append(chr(acc))
    return ''.join(result)

