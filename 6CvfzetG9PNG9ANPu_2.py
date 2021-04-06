
key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],
       ['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'],
       ['q', 'd']]
d = dict()
for p in key:
    d[p[0]] = p[1]
    d[p[1]] = p[0]
​
def mubashir_cipher(msg):
    return "".join(d[c] if c in d else c for c in msg)

