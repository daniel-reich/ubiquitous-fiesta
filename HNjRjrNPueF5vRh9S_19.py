
def hamming_code(message):
    z = [bin(ord(x))[2:].zfill(8) for x in message]
    return ''.join([3*i for x in z for i in x])

