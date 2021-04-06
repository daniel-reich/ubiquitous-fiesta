
def kix_code(addr):
    import re
    l2 = addr.upper().split(', ')
    l3 = [l2[2].split(), l2[1].split()]
    l3[0].pop(-1)
    l3[1].pop(0)
    
    l4 = [l3[1][-1]]
    if not re.search('[0-9]', l3[1][-1]) and len(l3) > 1:
        l4 = [l3[1][-2], l3[1][-1]]
    s_out = ''.join(l3[0][:2])
    if l4[0].isnumeric():
        s_out += l4[0]
    else:
        s_out += re.sub('[^0-9,^A-Z,^a-z]', 'X', l4[0])
    for i in range(1, len(l4)):
        if l4[i].isnumeric():
            s_out += l4[i]
        else:
            s_out += 'X' + l4[i]
    return s_out

