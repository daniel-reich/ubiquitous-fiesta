
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  ciphertext = ''
  for l in message:
    if l not in 'abcdefghijklmnopqrstuvwxyz':
      ciphertext += l
    else:
      for k in key:
        if l in k:
          ciphertext += k[0] if l == k[1] else k[1]
          break
  return ciphertext

