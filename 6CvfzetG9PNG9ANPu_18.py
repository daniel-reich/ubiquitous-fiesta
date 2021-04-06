
def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z
​
​
def mubashir_cipher(message):
    key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'],
           ['s', 'v'], ['h', 'x'], ['i', 'z'], ['r', 'y'],
           ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
    k_key1 = [x for y in key for x in y][0::2]
    k_key2 = [x for y in key for x in y][1::2]
    d1 = dict(zip(k_key1, k_key2))
    d2 = dict(zip(k_key2, k_key1))
    d = merge_two_dicts(d1, d2)
    return message.translate(str.maketrans(d))

