
def magic(txt):
  m, d, y = txt.split()
  return y.endswith(str(int(m) * int(d)))

