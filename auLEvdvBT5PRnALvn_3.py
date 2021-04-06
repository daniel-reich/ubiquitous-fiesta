
def mirror_cipher(message, key = 'abcdefghijklmnopqrstuvwxyz'):
    message = message.lower()
    idx = len(key)
    
    # mirror_idx = (mirror len - idx of first occur) - 1
    enc = []
​
    for letter in message:
        if letter in key:
            mirror_idx = idx - key.find(letter)
            enc.append(key[mirror_idx-1])
        else:
            enc.append(letter)
        
    return "".join(enc)

