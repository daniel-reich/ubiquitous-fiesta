
def digital_cipher(message, key):
    key = str(key)
    k = 0
    myans = []
​
    for i in range(len(message)):
        myans.append(ord(message[i])-96 + int(key[k]))
        k = (k + 1) % len(key)
    return myans

