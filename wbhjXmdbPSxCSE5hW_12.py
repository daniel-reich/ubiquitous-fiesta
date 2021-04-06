
def sigilize(desire):
  res = []
  for ch in desire[::-1]:     
    if ch.upper() not in 'AEIOU ' and ch not in res:
      res.append(ch)
  return ''.join(res).upper()[::-1]

