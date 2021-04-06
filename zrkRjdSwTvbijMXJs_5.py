
def encrypt(plncode, pad):
    lpln = [int(Z) for Z in plncode]
    lpad = [int(Z) for Z in pad[5:]]
    keyid = pad[:5]
    b0 = lambda x: x + 10 if x < 0 else x
    lo = [str(b0(Z[0] - Z[1])) for Z in zip(lpln, lpad)]
    return keyid + ''.join(lo)
​
​
def decrypt(cypcode, pad):
    lcyp = [int(Z) for Z in cypcode]
    lpad = [int(Z) for Z in pad]
    if lcyp[:5] != lpad[:5]:
        return "Error: Key IDs don't match."
    o10 = lambda x: x - 10 if x > 10 else x
    lo = [str(o10(Z[0] + Z[1])) for Z in zip(lcyp[5:], lpad[5:])]
    return ''.join(lo)

