
def mubashir_cipher(message):
    key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
    mubashir_dict = {}
    for x in key:
        mubashir_dict[x[0]] = x[1]
        mubashir_dict[x[1]] = x[0]
    res = ""
    for m in message:
        if m in mubashir_dict:
            res += mubashir_dict[m]
        else:
            res += m
    return res

