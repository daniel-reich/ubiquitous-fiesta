
def choose_fuse(fuses, current):
  a=sorted(int(i[:-1]) for i in fuses)
  for i in a:
    if i>=float(current[:-1]):
      return str(i)+'V'

