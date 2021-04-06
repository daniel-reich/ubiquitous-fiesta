
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  s=""
  for i in message:
    found=False
    for j in key:
      if i==j[0]:
        found=True
        s+=j[1]
        break
      elif i==j[1]:
        found=True
        s+=j[0]
        break
    if not found:
      s+=i
  return s

