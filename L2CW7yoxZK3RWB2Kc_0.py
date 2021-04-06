
import itertools
def nico_cipher(msg, key):
    l = len(key)
    pack =[list(key)]+list(list(msg[i:i+l]) for i in range(0,len(msg),l))
    tosort = itertools.zip_longest(*pack,fillvalue=" ")
    return "".join(["".join(i) for i in zip(*sorted(tosort, key=lambda col: col[0].lower()))][1:])

