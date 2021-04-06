
def num_split(num):
    s = []
    i = len(str(abs(num)))
    while i != 0:
        if num > 0:
            s.append(num//(10**(i-1))*(10**(i-1)))
            num -= num//(10**(i-1))*(10**(i-1))
            i -= 1
        else:
            s.append(-(abs(num) // (10 ** (i - 1)) * (10 ** (i - 1))))
            num += abs(num) // (10 ** (i - 1)) * (10 ** (i - 1))
            i -= 1
    return s

