
def shift_letter(c, shift):
    if c.isalpha():
        shifted_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        shifted_c = c
    return shifted_c
​
def paul_cipher(txt):
    shift, res, txt = 0, [], txt.upper()
    for i, c in enumerate(txt):
        if i == 0:
            res.append(c)
        else:
            res.append(shift_letter(c, shift))
        if c.isalpha():
            shift = ord(c) - ord('A') + 1
        #print(shift)
    return "".join(res)

