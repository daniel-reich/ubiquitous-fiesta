
def mirror_cipher(message,key = 'abcdefghijklmnopqrstuvwxyz'):
    return ''.join([key[len(key) - (key.index(char)+1)] if char in key else char for char in message.lower()])

