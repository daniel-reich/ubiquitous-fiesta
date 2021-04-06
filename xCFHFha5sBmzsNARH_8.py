
def reverse(txt):
  if not txt: return txt
  return reverse(txt[1:]) + txt[0]

