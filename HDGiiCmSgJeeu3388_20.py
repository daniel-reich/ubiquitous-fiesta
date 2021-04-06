
def choose_fuse(fuses, current):
  fuses = [int(i[:-1]) for i in fuses if int(i[:-1]) >= float(current[:-1])]
  return str(min(fuses))+"V"

