
class Cipher:
​
  def __init__(self, key):
    self.k = {}
    
    for lst in key:
      self.k[lst[0]] = lst[1]
      self.k[lst[1]] = lst[0]
  
  def encrypt(self, msg):
    nm = ''
    
    for l8r in msg:
      try:
        nm += self.k[l8r]
      except KeyError:
        nm += l8r
    
    return nm
​
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  
  cipher = Cipher(key)
  
  return cipher.encrypt(message)

