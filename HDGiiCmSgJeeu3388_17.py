
def choose_fuse(fuses, current):
  min_value = min(int(i[:-1]) for i in fuses if float(i[:-1]) >= float(current[:-1]))
  return str(min_value) + 'V'

