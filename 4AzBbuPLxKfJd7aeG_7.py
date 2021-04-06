
def encrypt(key, message):
    dkey = {}
    
    for i in range(len(key)):
        if i % 2 == 0:
            if key[i] not in dkey:
                dkey[key[i]] = key[i+1]
        else:
            if key[i] not in dkey:
                dkey[key[i]] = key[i-1]
    
    myans = ''
    for i in message:
        if i in dkey:
            myans += dkey[i]
        else:
            myans += i
    return myans

