
def choose_fuse(fuses, current):
  c=float(current[:-1])
  f=sorted([float(x[:-1]) for x in fuses]+[c])
  v=f[f.index(c)+1]
  if not v%1:
    return "{}V".format(int(v))
  else:
    return "{}V".format(v)

