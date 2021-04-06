
def encrypt(plncode, pad):
    len_plncode = len(plncode)
    len_pad = len(pad)
    if len_pad < len_plncode + 5:
        return "Error: Key IDs don't match."
    
    result = pad[:5]
    for i in range(len_plncode):
        result += str((int(plncode[i]) - int(pad[i+5]))%10)
    
    return result
​
def decrypt(plncode, pad):
    len_plncode = len(plncode)
    len_pad = len(pad)
    if len_pad < len_plncode:
        return "Error: Key IDs don't match."
    
    result = ""
    if pad[:5] != plncode[:5]:
        return "Error: Key IDs don't match."
    for i in range(5,len_plncode):
        result += str((int(plncode[i]) + int(pad[i]))%10)
    
    return result

