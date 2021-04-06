
def reversed_binary_integer(num):
    bi = bin(num)[2:]
    return int(bi[::-1], 2)

