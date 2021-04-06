
def mubashir_cipher(message):
  key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  res = ''
  for letter in message:
    for pair in key:
      if letter == pair[0]:
        res += pair[1]
        break
      elif letter == pair[1]:
        res += pair[0]
        break
    else:
      res += letter
  return res

