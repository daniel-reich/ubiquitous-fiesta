
def hamming_code(message):
    code = ""
    for c in message:
        for b in bin(ord(c))[2:].zfill(8):
            code += b * 3
    return code

