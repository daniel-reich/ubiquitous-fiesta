
def capital_letters(txt):
  c = 0
  for t in txt:
    if str(t).isupper():
      c += 1
  return c

