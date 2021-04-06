
def choose_fuse(fuses, current):
  return str(int(min([float(i[0:-1]) for i in fuses if float(i[0:-1])>=float(current[0:-1])])))+'V'

