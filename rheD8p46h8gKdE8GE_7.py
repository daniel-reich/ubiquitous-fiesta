
def grayscale(lst):
  return [[[max(round(sum(min(255,n) for n in l)/3),0)]*3 for l in ls] for ls in lst]

