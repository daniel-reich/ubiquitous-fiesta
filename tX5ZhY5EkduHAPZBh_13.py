
def nearest_element(n, lst):
  l = [(abs(n-x),x,i) for i, x in enumerate(lst)]
  return  sorted(l, key= lambda x: (x[0], -x[1]))[0][2]

