
def difference_two(lst):
  arr = []
  for x in lst:
    if x+2 in lst:
      arr.append([x,x+2])
  return sorted(arr)

