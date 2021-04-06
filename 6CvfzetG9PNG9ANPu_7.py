
import string
​
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  first = ''.join(x[0] for x in key)
  second = ''.join(x[1] for x in key)
  table = message.maketrans(first, second) 
  table.update(message.maketrans(second, first))
  return message.translate(table)

