
def num_of_sublists(lst):
  count = 0
  for item in lst:
    if isinstance(item,list):
      count += 1
  return count

