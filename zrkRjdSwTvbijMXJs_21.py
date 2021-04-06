
def encrypt(plncode, pad):
    ans = pad[:5]
    pi = 5
    for x in plncode: 
        ans += str((int(x)-int(pad[pi])) % 10)
        pi += 1       
    return ans
  
def decrypt(cypcode, pad):
    ans = ''
    if cypcode[:5] != pad[:5]:
        return "Error: Key IDs don't match." 
    for i in range(5, len(cypcode)):
        ans += str((int(pad[i])+int(cypcode[i])) % 10)
    return ans

