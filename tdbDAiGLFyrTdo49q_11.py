
def find_difference(a, b):
  vol = lambda lst: eval('*'.join(str(n) for n in lst))
  return abs(vol(a) - vol(b))

