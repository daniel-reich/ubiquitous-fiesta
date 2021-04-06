
from numpy import searchsorted
​
def choose_fuse(fuses, current):
  fuses = sorted(float(f[:-1]) for f in fuses)
  current = float(current[:-1])
  return "{:.0f}V".format(fuses[searchsorted(fuses, current)])

