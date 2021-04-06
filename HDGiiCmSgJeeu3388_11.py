
def choose_fuse(fuses, current):
  sort = sorted(fuses, key = lambda x: eval(x[:-1]))
  return [i for i in sort if eval(i[:-1]) >= eval(current[:-1])][0]

