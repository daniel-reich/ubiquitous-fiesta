
def sum_of_slices(lst):
  s = 0
  slices = []
  for i in lst:
    if s + i <= 100:
      s = s + i
    else:
      slices.append(s)
      s = i
  slices.append(s)
  return slices

