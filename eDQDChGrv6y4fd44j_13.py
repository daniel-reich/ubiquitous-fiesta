
def can_put(txt, dim):
  txt = txt.split()
  r, c = dim
  if max(len(wrd) for wrd in txt) > c:
    return False
  row = ""
  for wrd in txt:
    row = ' '.join((row, wrd)) if row else wrd
    if len(row) > c:
      row = wrd
      r -= 1
  return r > 0

