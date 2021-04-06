
def nearest_element(n, lst):
  t = sorted(lst, reverse=True)
  ans = sorted(t, key=lambda x: abs(x-n))
  return lst.index(ans[0])

