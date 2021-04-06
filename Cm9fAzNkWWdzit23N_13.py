
def wave(txt):
  res = []
  for i, j in enumerate(txt):
    res.append(txt[:i] + txt[i].upper() + txt[i+1:])
  
  if res:
    return [k for k in res if k.islower() == False and k != ' ']
  else:
    return res

