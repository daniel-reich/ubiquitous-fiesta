
def rolling_cipher(txt, n):
    s =''
    for char in txt:
        z = ord(char) + n
        if (z > 122):z=z-26
        elif (z < 97):z=z+26
        s+=chr(z)
    return s

