
def choose_fuse(fuses, current):
  arr = sorted(fuses + [current], key=lambda x: float(x[:-1]))
  return arr[arr.index(current) + 1]

