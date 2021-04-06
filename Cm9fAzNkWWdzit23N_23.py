
def wave(txt):
  txtlist = [list(txt) for i in txt]
  out = []
  for ind, i in enumerate(txtlist):
    if i[ind] != ' ':
      i[ind] = i[ind].upper()
      out.append(''.join(i))
  return out

