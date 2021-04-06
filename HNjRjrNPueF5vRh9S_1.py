
def hamming_code(message):
    encoded = ''.join(''.join(b * 3 for b in bin(ord(c))[2:].zfill(8)) for c in message)
    return encoded

