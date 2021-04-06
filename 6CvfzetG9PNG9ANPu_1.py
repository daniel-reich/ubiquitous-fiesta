
def mubashir_cipher(message):
  key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  d = dict(key)
  d.update(map(reversed, key))
  return ''.join(d.get(i, i) for i in message)

