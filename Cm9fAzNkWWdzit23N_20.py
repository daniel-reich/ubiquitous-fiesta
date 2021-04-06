
def wave(txt):
  lst = []
  for idx, c in enumerate(txt):
    if c.isalpha():
      lst.append(txt[:idx] + txt[idx].upper() + txt[idx + 1:])
  return lst

