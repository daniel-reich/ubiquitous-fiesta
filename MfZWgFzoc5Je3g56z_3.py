
def translate(ran, num):
    rsq = ran * ran
    if num > rsq: return '{} is not in the range [0:{}]'.format(num, rsq)
    snum = rsq - num
    l, r = (num + rsq - snum + 1, snum - num) if snum >= num else (num - snum, snum + rsq - num + 1)
    if l == r:
        s = '+{} or -{}'.format(l, l)
    elif l < r:
        s = str(-l)
    else:
        s = '+' + str(r)
    return '{} ---> {}'.format(s, snum)

