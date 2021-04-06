
def sum_of_slices(lst):
  slices = [[]]
  slice_no = 0
  for val in lst:
    if sum(slices[-1], val) < 100:
      slices[-1].append(val)
    else:
      slices.append([val])
​
  return [sum(slice) for slice in slices]

