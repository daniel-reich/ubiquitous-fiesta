
def nearest_element(n, lst):
  d = [abs(x-n) for x in lst]
  return max((i for i,x in enumerate(d) if x==min(d)), key = lst.__getitem__)

