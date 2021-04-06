
def modify(txt):
    z = ''.join([str(1+ord(x)-ord('a')) for x in txt[::-1]])
    return int((bin(int(z))[2:]))

