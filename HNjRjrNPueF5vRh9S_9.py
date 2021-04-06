
def hamming_code(message):
    return ''.join(list(map(lambda x:''.join(list(map(lambda x:x*3,list(bin(ord(x))[2:].zfill(8))))),list(message))))

