
def difference_two(lst):
  return sorted([[k, k+2] for k in lst if k+2 in lst])

