
import re
def playfair(txt, keyword):
    dirn = 1 if ' ' in txt else -1
    cipher = [c.upper() for i, c in enumerate(keyword) if i == 0 or keyword.find(c, 0, i) < 0]
    cipher += [c for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if not c in cipher]
    txt = re.sub('[.: ]', '', txt.upper()).replace('J', 'I')
​
    def encode(cc):
        i1, i2 = cipher.index(cc[0]), cipher.index(cc[1])
        r1, c1, r2, c2 = i1//5, i1%5, i2//5, i2%5
        if r1 == r2:
            return cipher[r1*5 + (c1+dirn)%5] + cipher[r2*5 + (c2+dirn)%5]
        elif c1 == c2:
            return cipher[((r1+dirn)%5)*5 + c1] + cipher[((r2+dirn)%5)*5 + c2]
        else:
            return cipher[r1*5 + c2] + cipher[r2*5 + c1]
​
    digraph, i = [], 0
    while i < len(txt):
        cc = txt[i:i+2]
        if len(cc) == 1 or cc[0] == cc[1]:
            cc = cc[0]+'X'
            i -= 1
        digraph.append(encode(cc))
        i += 2
​
    return ''.join(digraph)

