
def capital_letters(txt):
  c=0
  for i in txt:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      c+=1
  return c

