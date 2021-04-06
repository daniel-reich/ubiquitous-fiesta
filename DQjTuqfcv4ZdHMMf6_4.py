
def kaprekar(num, ctr=0):
    if num == 6174:
        return ctr
    s = str(num).zfill(4)
    a = int(''.join(sorted(s)))
    b = int(''.join(sorted(s, reverse=True)))
    x = kaprekar(b-a, ctr+1)
    return x

