
def unrepeated(txt):
  l = []
  for i in txt:
    if i not in l:
      l.append(i)
  return ''.join(l)

