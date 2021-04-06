
def choose_fuse(fuses, current):
  f = lambda x: float(x[:-1])
  return min((i for i in fuses if f(i)>=f(current)),key=lambda x: f(x))

