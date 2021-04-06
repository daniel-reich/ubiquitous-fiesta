
def modify(txt):
    return int(bin(int("".join(str(ord(c) - 96) for c in txt[::-1])))[2:])

