
def wave(txt):
  if len(txt)==0: return []
  res = []
  for i in range(len(txt)):
    if txt[i].isalpha():
      res.append(txt[0:i] + txt[i].upper() + txt[i+1:])
  return res

