
def hamming_code(message):
    buf = ''.join([format(ord(x), '08b') for x in message])
    return ''.join(x * 3 for x in buf)

