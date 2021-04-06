
def alphabet_index(txt):
  alpha='abcdefghijklmnopqrstuvwxyz'
  ret = []
  for c in txt:
    if c.isalpha(): ret.append(str(alpha.index(c.lower())+1))
  return ' '.join(ret)

