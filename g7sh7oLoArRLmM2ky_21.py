
letters = [chr(k) for k in range(65, 91)] + [chr(k) for k in range(97, 123)]
​
def decode(cipher):
    cipher = [c for c in cipher if c in letters]
    for i in range(len(cipher)):
        if 'A' <= cipher[i] <= 'Z':
            cipher[i] = '0'
        else:
            cipher[i] = '1'
    msg = ""
    for k in range(len(cipher) // 5):
        chunk = cipher[5*k:5*k+5]
        a = int("0b" + ''.join(chunk), 2)
        if a <= 25:
            msg += chr(97 + a)
        elif a == 30:
            msg += '.'
        elif a == 31:
            msg += ' '
        else:
            assert False, "Something is fishy here...."
    return msg
​
def encode(msg, mask):
    mask = [c for c in mask]
    idx = 0
    for char in msg:
        code = -1
        if char == ' ':
            code = 31
        elif char == '.':
            code = 30
        elif 'a' <= char.lower() <= 'z':
            code = ord(char.lower()) - 97
        if code >= 0:
            b = bin(code)[2:].zfill(5)
            for i in range(5):
                while not mask[idx].isalpha():
                    idx += 1
                if b[i] == '0':
                    mask[idx] = mask[idx].upper()
                else:
                    mask[idx] = mask[idx].lower()
                idx += 1
    cipher = ''.join(mask)
    return cipher
​
def baconify(msg, mask=None):
    if mask == None:
        # decipher message:
        return decode(msg)
    else:
        # encipher message:
        return encode(msg, mask)

