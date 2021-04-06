
def hamming_code(message):
    return "".join("".join(d * 3 for d in "{:0>8}".format(bin(ord(c))[2:]))
                   for c in message)

