
def mirror_cipher(msg,key='abcdefghijklmnopqrstuvwxyz'):
    Final = ''
    for item in range(len(msg)):
        if msg[item].lower() in key:
            z = -key.index(msg[item].lower())-1
            Final += key[z]
        else:
            Final += msg[item].lower()
    return Final

