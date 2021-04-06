
import functools
def mubashir_cipher(message):
  res=""
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  for i in str(message):
    test=""
    for j in key:
      if i in j:
        res=res+[o for o in j if o!=i][0]
        test="assita"
    if(test==""):
      res=res+i
  return res

