
def choose_fuse(fuses, c):
  return min((f for f in fuses if float(f[:-1])>=float(c[:-1])), key = lambda f: float(f[:-1]))

