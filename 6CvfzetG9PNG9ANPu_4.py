
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  key2=[x[::-1] for x in key]
  D=dict(key+key2)
  res=''
  for x in message:
    if x in D:
      res+=D[x]
    else:
      res+=x
  return res

