
def magic(txt):
  t = txt.split()
  n = int(t[0])*int(t[1])
  return t[2].endswith(str(n))

