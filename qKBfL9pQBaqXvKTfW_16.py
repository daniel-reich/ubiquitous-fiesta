
def sum_of_slices(lst):
  slices = []
  c = 0
  for num in lst:
    if c+num > 100:
      slices += [c]
      c = num
    else:
      c += num
  return slices + [c]

