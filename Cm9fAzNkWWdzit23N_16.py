
def wave(txt):
  res = []
  for i in range(len(txt)):
    if txt[i] == " ": continue
    word = txt[0:i] + txt[i].upper() + txt[i+1:]
    res.append(word)
  return res

