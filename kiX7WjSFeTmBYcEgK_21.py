
def major_sum(lst):
  a = sum([i for i in lst if i < 0])
  b = sum([i for i in lst if i > 0])
  c = lst.count(0)
  return a if abs(a) > b else max(b, c)

