
def major_sum(lst):
  p = sum(n for n in lst if n > 0)
  n = sum(n for n in lst if n < 0)
  z = lst.count(0)
  return n if -n > p and -n > z else max(p, z)

