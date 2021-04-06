
def wave(txt):
  lst = []
  for i in range(len(txt)):
    chars = list(txt)
    if chars[i] == ' ':
      continue
    chars[i] = chars[i].upper()
    s = ''.join(chars)
    lst.append(s)
  return lst

