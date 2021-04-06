
def choose_fuse(fuses, current):
  return min([x for x in fuses if float(x[:-1]) >= float(current[:-1])], key=lambda x: int(x[:-1]))

