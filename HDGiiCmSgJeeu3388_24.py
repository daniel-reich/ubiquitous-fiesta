
def choose_fuse(fuses, current):
  return "{}V".format(sorted([i for i in list(map(lambda x:int(x[:-1]),fuses)) if float(current[:-1])<=float(i)])[0])

