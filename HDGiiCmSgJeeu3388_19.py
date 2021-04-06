
def choose_fuse(f, c):
​
  f = [int(e[:-1]) for e in f if float(e[:-1]) >= float(c[:-1])]
  return str(min(f))+'V'

