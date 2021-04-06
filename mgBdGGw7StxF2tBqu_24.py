
def duplicates(txt):
  c = 0
  for i in txt:
    if txt.count(i) >= 2:
      c += txt.count(i) - 1
      txt = txt.replace(i, '')
  return c

