
def alternate_sort(lst):
  res = []
  chars = sorted([c for c in lst if type(c) == str])
  digits = sorted([d for d in lst if type(d) == int])
  for i in range(len(chars)):
    res.extend([digits[i],chars[i]])
  return res

