
def mubashir_cipher(txt):
  key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]  
  res = ''
  for i in txt: 
    if i.isalpha():
      item = [j for j in key if i in j][0]
      res += item[0] if i == item[1] else item[1]
    else:
      res += i
  return res

