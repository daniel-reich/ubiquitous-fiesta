
def isbn13(txt):
    l13 = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    l10 = [10,9,8,7,6,5,4,3,2,1]
    if len(txt) == 13 and txt[:3] == '978' and sum(int(x) * l13[i] for i, x in enumerate(txt)) % 10 == 0:
        return 'Valid'
    elif len(txt) == 10 and sum(int(x) * l10[i] if x not in ['X','x'] else 10 * l10[i] for i, x in enumerate(txt)) % 11 == 0:
        txt = '978' + txt
        return txt[:-1] + str(10 - sum(int(x) * l13[i] for i, x in enumerate(txt[:-1])) % 10)
    else:
        return 'Invalid'

