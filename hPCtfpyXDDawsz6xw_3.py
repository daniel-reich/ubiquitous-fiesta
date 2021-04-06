
def verbify(txt):
  
  words = txt.split()
  
  if words[0][-1] == 'e':
    words[0] += 'd'
  elif words[0][-2:] == 'ed':
    words[0] = words[0]
  else:
    words[0] += 'ed'
  
  return ' '.join(words)

