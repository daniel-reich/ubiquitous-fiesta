
def choose_fuse(fuses, current):
  return sorted([fuse for fuse in fuses if float(fuse[:-1]) >= float(current[:-1])] , key = lambda fuse : float(fuse[:-1]))[0]

