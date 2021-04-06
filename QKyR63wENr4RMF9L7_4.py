
import string
def tweak_letters(s, lst):
    l=[]
    seq=string.ascii_lowercase
    for x, y in zip(s, lst):
        l.append(seq[(seq.index(x)+y)%26])
    return "".join(l)

