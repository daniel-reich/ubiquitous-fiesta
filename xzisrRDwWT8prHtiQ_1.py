
def difference_two(lst):
  lst.sort()
  return [[a,a+2] for a in lst if a+2 in lst]

