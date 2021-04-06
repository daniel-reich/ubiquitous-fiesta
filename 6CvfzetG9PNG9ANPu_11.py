
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'],
        ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'],
        ['t', 'f'], ['q', 'd']]
  a = ""
  for i in message:
      for j in key:
          if i in j:
              a += [k for k in j if k!=i][0]
              break
      else:
          a += i
  return a

