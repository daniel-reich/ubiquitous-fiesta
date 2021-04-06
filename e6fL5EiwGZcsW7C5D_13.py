
def alph_num(txt):
  l = []
  for i in txt:
    l.append(str(ord(i) - 65))
  return ' '.join(l)

