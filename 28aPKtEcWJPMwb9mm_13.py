
def modify(txt):
    return int(bin(int(''.join(list(map(lambda x:str(ord(x)-96),list(txt[::-1]))))))[2:])

