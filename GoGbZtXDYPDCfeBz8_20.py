
def magic(txt):
  d,m,y=txt.split()
  return y.endswith(str(int(d)*int(m)))

