
def wave(txt):
  lst = []
  for i in range(len(txt)):
    if not txt[i].isspace():
      lst.append(txt[:i] + txt[i].upper() + txt[i+1:])
  return lst

