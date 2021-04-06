
def unique(l):
  return sorted(l)[0] if sorted(l)[0] != sorted(l)[1] else sorted(l)[-1]

