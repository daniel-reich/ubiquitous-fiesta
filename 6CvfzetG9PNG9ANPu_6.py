
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  k2 = {i[0]:i[1] for i in key}
  for j in key:
    k2[j[1]]=j[0]
  output = ""
  for i in message:
    if i in k2:
      output += k2[i]
    else:
      output += i
  return output

