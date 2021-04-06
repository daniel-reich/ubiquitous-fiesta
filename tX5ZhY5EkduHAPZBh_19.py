
def nearest_element(n, lst):
  l = sorted(lst)
​
  d = {abs(i - n): i for i in l}
  d = sorted(d.items(), key = lambda x: x)
  res = d[0][-1]
  return(lst.index(res))

