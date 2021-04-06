
def difference_two(lst):
  return sorted([[i,i+2] for i in lst if i+2 in lst])

