
def verbify(txt):
  res= txt.split()
  if res[0][-2:] == 'ed':
    return ' '.join(res)
  elif res[0][-1] == 'e':
    res[0] += 'd'
  else:
    res[0] += 'ed'
  return ' '.join(res)

