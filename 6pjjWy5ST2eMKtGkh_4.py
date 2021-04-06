
def replace(txt, r):
  for i in txt:
    if r[0] <= i <= r[2]:
      txt = txt.replace(i, '#')
  return txt

