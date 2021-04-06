
def mirror_cipher(message,key='1'):
    if key == '1':
        key = 'abcdefghijklmnopqrstuvwxyz'
    if key == '':
        return message
    myans = ''
    for i in range(len(message)):
        if message[i].lower() in key:
            a = len(key) - key.index(message[i].lower())- 1
            myans += key[a]
        else:
            myans += message[i].lower()
​
    return myans

