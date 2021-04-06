
def choose_fuse(fuses, current):
  current = float(current[:-1])
  for f in sorted(int(i[:-1]) for i in fuses):
    if current <= f:
      return str(f)+"V"

