
def paul_cipher(txt):
    myans = ''
    for i in range(len(txt)):
        if txt[i].isalpha():
            myans += txt[i].upper()
            ctr = ord(txt[i].upper())-64
            break
        else:
            myans += txt[i]
    i += 1
​
    for j in range(i,len(txt)):
        if txt[j].isalpha():
            myans += chr((((ord(txt[j].upper())-64) + ctr-1) % 26)+65)
            ctr = ord(txt[j].upper())-64
        else:
            myans += txt[j]
​
    return myans

