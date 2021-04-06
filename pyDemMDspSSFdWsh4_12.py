
def digital_decipher(eMessage, key):
    myans = ''
    for i in range(len(eMessage)):
        ii = i % len(str(key))
        myans += chr(eMessage[i] - int(str(key)[ii]) + 96)
    return myans

