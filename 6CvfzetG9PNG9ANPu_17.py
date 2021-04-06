
def mubashir_cipher(message):
  key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  res = ""
  for char in message:
    if char.isalpha():
      pair = [p for p in key if char in p][0]
      res+=pair[1] if pair[0]==char else pair[0]
    else:
      res+=char
  return res

