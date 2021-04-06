
def mubashir_cipher(message):
  fwkey = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  revkey = [[x[1], x[0]] for x in fwkey]
  key=dict(fwkey + revkey)
  
  decoded=''
​
  for char in message:
    if char not in key:
      print ("%s is not in keys" % char)
      decoded += char
    else:
      decoded += key[char]
  return(decoded)

