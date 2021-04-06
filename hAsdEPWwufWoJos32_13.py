
def no_yelling(phrase):
  backwards = phrase[::-1]
  count = 0
  if backwards[0] == '?':
    t = '?'
  elif backwards[0] == '!':
    t = '!'
  else:
    return phrase
  x = t
  i = 0
  if backwards[1] == x:
    while backwards[i] == x:
      i+= 1
    return (phrase[0:-i+1])
  return phrase

